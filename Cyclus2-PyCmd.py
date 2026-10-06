#!/usr/bin/env python3
#
# PURPOSE: An interactive "chat-like" command-line interface to Cyclus2.
# AUTHORS: Johannes Keyser <johannes.keyser@uni-hamburg.de>
# LICENSE: EUPL-1.2
# SUMMARY: This script connects to a Cyclus2 ergometer and allows the user
#          to interactively type commands like "data?", along with some
#          convenience features like a built-in command reference.
#
# SPDX-FileCopyrightText: Johannes Keyser <johannes.keyser@uni-hamburg.de>
# SPDX-License-Identifier: EUPL-1.2

import argparse
import socket
import sys
import threading
from pathlib import Path

import serial
import yaml
from prompt_toolkit.application import Application
from prompt_toolkit.clipboard.pyperclip import PyperclipClipboard
from prompt_toolkit.document import Document
from prompt_toolkit.filters import has_focus
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.layout.containers import HSplit, Window, Float, FloatContainer
from prompt_toolkit.layout.layout import Layout
from prompt_toolkit.widgets import TextArea, Dialog
from prompt_toolkit.layout.dimension import Dimension
from prompt_toolkit.completion import Completer, Completion
from prompt_toolkit.layout.controls import FormattedTextControl


def read_version() -> str:
    """Read the project version from the bundled VERSION file."""
    # NOTE: In a download/checkout, the VERSION file sits next to the script.
    #       This assumes PyInstaller handles this well in its file bundling.
    base_dir = Path(__file__).resolve().parent
    return (base_dir / "VERSION").read_text(encoding="utf-8").strip()


VERSION = read_version()
DEFAULT_ADDRESS = "192.168.1.200"  # a local address as default/example
DEFAULT_PORT = 25000  # port of the Cyclus2 Ethernet/TCP interface
DEFAULT_SERIAL_BAUDRATE = 4800  # the Cyclus2 serial default after power-up
READ_TIMEOUT = 0.25  # seconds the reader thread waits for data before re-checking

# Write "Cyclus2-PyCmd" in ASCII art font "Small Slant"; yes, that is important.
ASCII_BANNER = (
    "Welcome to\n"
    + "   _____         __         ___     ___       _____         __\n"
    + "  / ___/_ ______/ /_ _____ |_  |___/ _ \\__ __/ ___/_ _  ___/ /\n"
    + " / /__/ // / __/ / // (_-</ __/___/ ___/ // / /__/  ' \\/ _  /\n"
    + " \\___/\\_, /\\__/_/\\_,_/___/____/  /_/   \\_, /\\___/_/_/_/\\_,_/\n"
    + f"     /___/                            /___/    version {VERSION}\n"
)

# Cyclus2 uses ASCII commands and a CRLF terminator on requests.
# Responses are plain ASCII and end with CR, with no trailing LF.
REQUEST_NEWLINE = b"\r\n"


# The command reference is kept as local project data at this location:
REF_PATH = Path(__file__).resolve().parent / "docs" / "command-reference"


def strip_html_comments(text: str) -> str:
    """
    Remove HTML-style comments while leaving the Markdown text intact.
    NOTE: Simple parser, no regexes, assumes the comment markers are plain.
    """
    result = []
    index = 0
    while index < len(text):
        start = text.find("<!--", index)
        if start == -1:
            result.append(text[index:])
            break
        result.append(text[index:start])
        end = text.find("-->", start + 4)
        if end == -1:
            break
        index = end + 3
    return "".join(result)


def strip_yaml_front_matter(text: str) -> str:
    """
    Remove an optional YAML front matter block from a Markdown file.
    NOTE: The project layout keeps YAML metadata in the opening block only.
    """
    cleaned = strip_html_comments(text).lstrip()
    if not cleaned.startswith("---\n"):
        return cleaned

    end = cleaned.find("\n---\n", len("---\n"))
    if end == -1:
        raise ValueError("Missing closing YAML front matter")
    return cleaned[end + len("\n---\n") :].lstrip()


def load_command_reference() -> dict:
    """Read the command reference files into a lookup table keyed by command name."""
    if not REF_PATH.exists():
        raise FileNotFoundError(f"Command reference directory not found: {REF_PATH}")

    catalog = {}
    # The project keeps native commands in one folder and Ergoline commands in another.
    for directory in (REF_PATH / "commands", REF_PATH / "ergoline"):
        if not directory.exists():
            raise FileNotFoundError(f"Command reference dir is missing: {directory}")

        for path in sorted(directory.glob("*.md")):
            if path.name.lower() == "readme.md":
                continue

            markdown = path.read_text(encoding="utf-8")
            body = strip_yaml_front_matter(markdown).strip()
            if not body:
                raise ValueError(f"Empty command reference in {path}")

            front_matter = strip_html_comments(markdown).lstrip()
            command_data = {}
            if front_matter.startswith("---\n"):
                marker_end = front_matter.find("\n---\n", len("---\n"))
                if marker_end == -1:
                    raise ValueError(f"Missing closing YAML front matter in {path}")

                yaml_text = front_matter[len("---\n") : marker_end]
                parsed = yaml.safe_load(yaml_text)
                if isinstance(parsed, dict):
                    command_data = parsed.get("command", {})

            name = str(command_data.get("name", path.stem)).strip()
            summary = str(command_data.get("summary", "")).strip()
            if not summary:
                summary = path.stem

            category = "ergoline" if path.parent.name == "ergoline" else "cyclus2"
            catalog[name] = {
                "name": name,
                "summary": summary,
                "body": body,
                "category": category,
            }

    return catalog


def list_command_names(command_catalog: dict) -> str:
    """
    List the available commands in the catalog, grouped by category.
    """
    groups = {"cyclus2": [], "ergoline": []}
    for name, record in sorted(command_catalog.items()):
        category = record.get("category", "cyclus2")
        groups.setdefault(category, []).append(name)

    sections = []
    for category_name, heading in (
        ("cyclus2", "Cyclus2 native commands:"),
        ("ergoline", "Ergoline-compatible commands:"),
    ):
        names = groups.get(category_name, [])
        if not names:
            continue
        lines = [heading]
        for name in names:
            summary = command_catalog[name].get("summary", "")
            if summary:
                lines.append(f"  {name}: {summary}")
            else:
                lines.append(f"  {name}")
        sections.append("\n".join(lines))

    if not sections:
        return "No command reference entries are available."
    return "\n\n".join(sections)


def format_command_help(command_catalog: dict, command_name: str) -> str:
    """
    Format the reference text for a specific command,
    or the list of available commands if the command is not found.
    """
    key = str(command_name).strip()
    if not key:
        return list_command_names(command_catalog)

    command_record = command_catalog.get(key)
    if command_record is None:
        message = f"Command not found: {command_name}\n\n"
        return message + list_command_names(command_catalog)

    body = command_record.get("body", "")
    plain_text = body.replace("`", "")
    return "\n" + plain_text.rstrip() + "\n"


def local_reply_for(command_catalog: dict, text: str):
    """
    HELP is handled by Cyclus2-PyCmd itself: It is never sent to the Cyclus2.
    Returns the reply text for a HELP command, or None if text is not a HELP command
    (and should be sent to the Cyclus2 instead).
    FIXME: Is this sensible?
    """
    if text == "HELP":
        return list_command_names(command_catalog)
    if text.startswith("HELP "):
        return format_command_help(command_catalog, text[len("HELP ") :].strip())
    return None


def printable_ascii(data: bytes) -> str:
    try:
        text = data.decode("ascii")
    except UnicodeDecodeError:
        text = data.decode("ascii", errors="replace")
    return text.rstrip("\r")  # strip trailing CR sent by Cyclus2


class SocketConnection:
    """
    Adapt a TCP socket to the small interface that Cyclus2Session expects,
    which pyserial's Serial objects already provide:
      read(size) -> bytes; b"" means "nothing arrived yet", None means "closed".
      write(data), close().
    """

    def __init__(self, sock: socket.socket):
        self.sock = sock

    def read(self, size: int):
        try:
            data = self.sock.recv(size)
        except socket.timeout:
            return b""
        return data if data else None  # recv() returns b"" if the peer closed

    def write(self, data: bytes):
        self.sock.sendall(data)

    def close(self):
        try:
            self.sock.shutdown(socket.SHUT_RDWR)
        except OSError:
            pass
        self.sock.close()


class Cyclus2Session:
    """
    A connection to the Cyclus2 (over TCP or serial), modeled as a two-way
    conversation. send_line() sends a message to the Cyclus2; any text the
    Cyclus2 replies is delivered to a callback as soon as it arrives, whenever
    that is. A background thread does the actual reading, because the Cyclus2
    does not always wait to be asked: For example, after command data=7,
    it keeps streaming data until command data=0.

    Use via_tcp() or via_serial() to create a session.
    """

    def __init__(self, connection):
        self.connection = connection
        self._on_message = lambda line: None
        self._running = True
        self._reader_thread = threading.Thread(target=self._read_loop, daemon=True)
        self._reader_thread.start()

    @classmethod
    def via_tcp(cls, host: str, port: int, timeout: float = 2.0):
        sock = socket.create_connection((host, port), timeout=timeout)
        # After connecting, use a short timeout so the reader thread regularly
        # checks whether the session was closed.
        sock.settimeout(READ_TIMEOUT)
        return cls(SocketConnection(sock))

    @classmethod
    def via_serial(cls, device: str, baudrate: int, timeout: float = 2.0):
        # The Cyclus2 serial interface uses 8 data bits, no parity, 1 stop bit
        # and no flow control; only the baud rate is configurable (see "br" command).
        connection = serial.Serial(
            port=device,
            baudrate=baudrate,
            bytesize=serial.EIGHTBITS,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            xonxoff=False,
            rtscts=False,
            dsrdtr=False,
            timeout=READ_TIMEOUT,
            write_timeout=timeout,
        )
        return cls(connection)

    def set_message_handler(self, callback):
        """Register the function to call for every line received from the Cyclus2."""
        self._on_message = callback

    def _read_loop(self):
        # Data may arrive in arbitrary pieces, so collect it until a complete
        # line (ended by CR, or LF/CRLF depending on the "eol" command) is there.
        buffer = b""
        while self._running:
            try:
                chunk = self.connection.read(1024)
            except OSError:  # includes serial.SerialException
                break  # the connection was closed or lost
            if chunk is None:
                break  # the peer closed the connection
            buffer += chunk.replace(b"\n", b"\r")  # treat LF like CR

            *lines, buffer = buffer.split(b"\r")  # the remainder is incomplete
            for raw_line in lines:
                line = printable_ascii(raw_line).strip()
                if line:  # a CRLF ending leaves an empty piece; skip it
                    self._on_message(line)

    def send_line(self, command: str):
        self.connection.write(command.encode("ascii") + REQUEST_NEWLINE)

    def close(self):
        self._running = False
        # Wait for the reader to stop first; closing a serial port while another
        # thread is still reading from it raises errors in that thread.
        if threading.current_thread() is not self._reader_thread:
            self._reader_thread.join()
        self.connection.close()


class Cyclus2Completer(Completer):
    """Create a completer for the Cyclus2 commands."""

    def __init__(self, command_catalog: dict):
        self.command_catalog = command_catalog

    def get_completions(self, document, complete_event):
        text = document.text_before_cursor

        # Complete HELP commands with the command reference.
        if text.upper().startswith("HELP "):
            prefix = text[5:].strip().lower()
            for name in sorted(self.command_catalog):
                if name.lower().startswith(prefix):
                    yield Completion(name, start_position=-len(prefix))
            return

        # Complete command names at the start of the line.
        prefix = text.strip().lower()
        for name in sorted(self.command_catalog):
            if name.lower().startswith(prefix):
                yield Completion(name, start_position=-len(prefix))


class ChatSession:
    """
    Runs the interactive chat: Everything the user sends and everything the
    Cyclus2 replies appears in the same scrolling transcript, with a single input
    line always available below it.
    HELP commands trigger a popup dialog to get out of the way of the chat log.
    Tab lets user complete the Cyclus2 commands from the reference.
    """

    def __init__(self, session: Cyclus2Session, command_catalog: dict):
        self.session = session
        self.command_catalog = command_catalog
        c2completer = Cyclus2Completer(command_catalog)
        self._active_popup = None
        session.set_message_handler(self._on_device_message)

        intro = (
            ASCII_BANNER
            + "\n"
            + "Type any Cyclus2 command or use HELP [command] for reference.\n"
            + "Press Tab to 'cycle through' or complete half-typed commands.\n"
            + "You can use the mouse to select text and copy it with Ctrl+C.\n"
            + "To end the session, type QUIT to disconnect from the Cyclus2.\n"
        )
        self.chatlog_area = TextArea(
            text=intro,
            read_only=True,
            focus_on_click=True,
            wrap_lines=True,
            scrollbar=True,
        )
        self.input_area = TextArea(
            height=1,
            prompt="Command> ",
            multiline=False,
            focus_on_click=True,
            wrap_lines=False,
            style="bg:darkgreen",
            completer=c2completer,
        )
        self.input_area.accept_handler = self._on_submit

        self.root_container = FloatContainer(
            content=HSplit(
                [self.chatlog_area, Window(height=1, char="─"), self.input_area]
            ),
            floats=[],
        )

        layout = Layout(self.root_container, focused_element=self.input_area)

        bindings = KeyBindings()

        @bindings.add("c-c")
        def _copy(event):
            # Only copies; ending the session is done with the QUIT command.
            buffer = self.chatlog_area.buffer
            if buffer.selection_state:
                event.app.clipboard.set_data(buffer.copy_selection())
                event.app.invalidate()

        @bindings.add("<any>", filter=has_focus(self.chatlog_area))
        def _type_in_input(event):
            # The chat history is not for typing: Send typed text to the command row.
            if event.data.isprintable():
                event.app.layout.focus(self.input_area)
                self.input_area.buffer.insert_text(event.data)

        def _dismiss_if_popup(event):
            if self._active_popup is not None:
                self._close_popup()
                event.app.invalidate()

        bindings.add("c-g")(_dismiss_if_popup)
        bindings.add("escape")(_dismiss_if_popup)

        self.app = Application(
            layout=layout,
            key_bindings=bindings,
            full_screen=True,
            mouse_support=True,
            clipboard=PyperclipClipboard(),
        )

    def _append(self, line: str):
        new_text = self.chatlog_area.text + line + "\n"
        self.chatlog_area.buffer.set_document(
            Document(new_text, cursor_position=len(new_text)), bypass_readonly=True
        )

    def _close_popup(self):
        if self._active_popup is not None:
            try:
                self.root_container.floats.remove(self._active_popup)
            except ValueError:
                pass
            self._active_popup = None

        # restore focus to input area, otherwise typing doesn't work
        self.app.layout.focus(self.input_area)
        self.app.invalidate()

    def _show_popup(self, title: str, text: str):

        help_area = TextArea(
            text=text,
            read_only=True,
            wrap_lines=True,
            scrollbar=True,
            height=Dimension(min=10, max=20),
        )

        tip_area = Window(
            height=1,
            content=FormattedTextControl(
                [
                    (
                        "fg:ansicyan italic",
                        "Press Esc or Ctrl-G to close this help window.",
                    )
                ]
            ),
            dont_extend_height=True,
            always_hide_cursor=True,
        )

        body = HSplit([help_area, Window(height=1, char="─"), tip_area])

        dialog = Dialog(
            title=title,
            body=body,
            buttons=[],
            width=Dimension(preferred=80),
            modal=False,
        )

        self._active_popup = Float(content=dialog)
        self.root_container.floats.append(self._active_popup)
        self.app.layout.focus(help_area)
        self.app.invalidate()

    def _on_submit(self, buffer):
        text = buffer.text.strip()
        if not text:
            return

        # Don't add HELP commands in the chat transcript.
        if not text.startswith("HELP"):
            # If a popup is open, close it as soon as the user continues normally
            if self._active_popup is not None:
                self._close_popup()
            self._append(f"\nCommand> {text}")

        if text == "QUIT":
            self.session.close()
            self.app.exit()
            return

        if text == "HELP":
            self._show_popup(
                "Available commands", list_command_names(self.command_catalog)
            )
            return

        if text.startswith("HELP "):
            cmd = text[5:].strip()
            self._show_popup(
                f"Help: {cmd}", format_command_help(self.command_catalog, cmd)
            )
            return

        self.session.send_line(text)

    def _on_device_message(self, text: str):
        self._append(f"Cyclus2> {text}")
        self.app.invalidate()

    def run(self):
        self.app.run()


def parse_args():
    parser = argparse.ArgumentParser(
        description="Interactively send commands to a Cyclus2 ergometer over TCP/IP or serial."
    )
    parser.add_argument(
        "--transport",
        choices=("tcp", "serial"),
        help="Connection type (default: tcp if --address is given, serial if "
        "--device is given, otherwise ask interactively).",
    )
    parser.add_argument(
        "--address",
        default=None,
        help=f"Cyclus2 IP address for TCP (default: {DEFAULT_ADDRESS}).",
    )
    parser.add_argument(
        "--device",
        help="Serial device path, e.g. /dev/ttyUSB0 or COM3.",
    )
    parser.add_argument(
        "--baudrate",
        type=int,
        default=DEFAULT_SERIAL_BAUDRATE,
        help=f"Serial baud rate (default: {DEFAULT_SERIAL_BAUDRATE}).",
    )
    parser.add_argument(
        "--help-command",
        metavar="COMMAND",
        help="Show the reference for a specific command.",
    )
    parser.add_argument(
        "--version",
        action="store_true",
        help="Show the project version and exit.",
    )
    args = parser.parse_args()
    if args.transport is None:
        # Infer the connection type from the other options, if possible.
        if args.device:
            args.transport = "serial"
        elif args.address:
            args.transport = "tcp"
    if args.transport == "tcp" and args.device:
        parser.error("--device can only be used with --transport serial")
    if args.transport == "serial" and args.address:
        parser.error("--address can only be used with --transport tcp")
    if args.baudrate <= 0:
        parser.error("--baudrate must be a positive integer")
    return args


def prompt(question: str, default: str) -> str:
    """
    Ask a question and return the answer, or the default if the answer is empty.
    Without an interactive terminal, nobody can answer, so use the default.
    """
    try:
        if sys.stdin.isatty():
            return input(f"{question} [default is {default}]: ").strip() or default
    except KeyboardInterrupt:
        print("\nReceived keyboard interrupt; aborting.")
        sys.exit(0)
    except EOFError:
        pass
    return default


def connect(args) -> Cyclus2Session:
    """
    Open the connection selected on the command line (TCP or serial).
    Anything not given there is asked for, e.g. after double-clicking the
    Windows executable, which starts the program without any arguments.
    """
    timeout = 2  # seconds for connecting and sending

    transport = args.transport or prompt(
        "Connect via network (tcp) or serial cable (serial)?", "tcp"
    )

    if transport == "serial":
        # USB-to-serial adapters are named differently per platform.
        if sys.platform == "win32":
            print("Hint: See Device Manager > Ports (COM & LPT) for your adapter.")
            default_device = "COM3"
        else:
            print("Hint: After plugging in the adapter, see `ls /dev/ttyUSB*`.")
            default_device = "/dev/ttyUSB0"
        device = args.device or prompt("Enter the serial device", default_device)
        print(
            f"Trying to connect to {device} at {args.baudrate} baud ... ",
            end="",
            flush=True,
        )
        return Cyclus2Session.via_serial(device, args.baudrate, timeout)

    if transport != "tcp":
        raise ValueError(f"unknown connection type {transport!r}, use tcp or serial")
    addr = args.address or prompt("Enter your Cyclus2 IP address", DEFAULT_ADDRESS)
    print(f"Trying to connect to {addr}:{DEFAULT_PORT} ... ", end="", flush=True)
    return Cyclus2Session.via_tcp(addr, DEFAULT_PORT, timeout)


def main():
    args = parse_args()

    if args.version:
        print(f"Cyclus2-PyCmd {VERSION}")
        return

    command_catalog = load_command_reference()

    if args.help_command:
        print(format_command_help(command_catalog, args.help_command))
        return

    print(ASCII_BANNER)

    try:
        session = connect(args)
    except (OSError, ValueError) as exc:  # e.g., unreachable host or no such device
        print("connection failed :(.")  # complete above message "Trying to connect..."
        print(
            "Please check the connection settings; is the Cyclus2 reachable on the "
            "selected interface?\n" + f"Connection error details: {exc}",
            file=sys.stderr,
        )
        sys.exit(1)

    print("connection success :).")

    try:
        ChatSession(session, command_catalog).run()
        # The chat log vanishes with the full-screen UI, so confirm on the terminal.
        print("Disconnected from the Cyclus2 and quit the session. Bye.")
    except KeyboardInterrupt:
        print("\nReceived keyboard interrupt; disconnecting.")
    except Exception as exc:
        print(
            f"ERROR: {exc}\n"
            + "Something went wrong with the script, see error above.\n"
            + "Ending the script now; try to restart it and/or report the error.",
            file=sys.stderr,
        )
        sys.exit(1)
    finally:
        session.close()


if __name__ == "__main__":
    main()
