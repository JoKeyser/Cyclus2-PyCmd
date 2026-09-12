#!/usr/bin/env python3
#
# PURPOSE: An interactive "chat-like" command-line interface to Cyclus2.
# AUTHORS: Johannes Keyser <johannes.keyser@uni-hamburg.de>
# LICENSE: EUPL-1.2
# SUMMARY: This script connects to a Cyclus2 ergometer over TCP/IP and
#          allows the user to interactively type commands like "data?".
#          It assumes that the Cyclus2 server is running and accessible
#          at the specified ADDRESS and PORT, see code below.
#
# SPDX-FileCopyrightText: Johannes Keyser <johannes.keyser@uni-hamburg.de>
# SPDX-License-Identifier: EUPL-1.2

import argparse
import socket
import sys
import threading
import time
from pathlib import Path

import yaml
from prompt_toolkit.application import Application
from prompt_toolkit.document import Document
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.layout.containers import HSplit, Window
from prompt_toolkit.layout.layout import Layout
from prompt_toolkit.widgets import TextArea



def read_version() -> str:
    """Read the project version from the bundled VERSION file."""
    # NOTE: In a download/checkout, the VERSION file sits next to the script.
    #       This assumes PyInstaller handles this well in its file bundling. 
    base_dir = Path(__file__).resolve().parent
    return (base_dir / "VERSION").read_text(encoding="utf-8").strip()


VERSION = read_version()
DEFAULT_ADDRESS = "192.168.1.200"  # a local address as default/example

# Write "Cyclus2-PyCmd" in ASCII art font "Small Slant"; yes, that is important.
ASCII_BANNER = (
 "Welcome to\n" + \
 "   _____         __         ___     ___       _____         __\n" +
 "  / ___/_ ______/ /_ _____ |_  |___/ _ \\__ __/ ___/_ _  ___/ /\n" +
 " / /__/ // / __/ / // (_-</ __/___/ ___/ // / /__/  ' \\/ _  /\n" +
 " \\___/\\_, /\\__/_/\\_,_/___/____/  /_/   \\_, /\\___/_/_/_/\\_,_/\n" +
f"     /___/                            /___/     version {VERSION}\n")

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
            catalog[name] = {"name": name,
                             "summary": summary,
                             "body": body,
                             "category": category}

    return catalog


def list_command_names(command_catalog : dict) -> str:
    """
    List the available commands in the catalog, grouped by category.
    """
    groups = {"cyclus2": [], "ergoline": []}
    for name, record in sorted(command_catalog.items()):
        category = record.get("category", "cyclus2")
        groups.setdefault(category, []).append(name)

    sections = []
    for category_name, heading in (("cyclus2", "Cyclus2 native commands:"),
                                   ("ergoline", "Ergoline-compatible commands:")):
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


def format_command_help(command_catalog : dict, command_name: str) -> str:
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
        return format_command_help(command_catalog, text[len("HELP "):].strip())
    return None



def recv_stream(sock, timeout=2.0, chunk_size=1024):
    """Read until the socket becomes idle for a short moment."""
    sock.settimeout(timeout)
    chunks = []
    deadline = time.monotonic() + timeout
    last_data_time = time.monotonic()
    TIMEOUT_LIMIT = 0.25  # idle time to consider the stream finished, in seconds

    while True:
        remaining = max(0.0, deadline - time.monotonic())
        if remaining <= 0:
            break

        sock.settimeout(min(remaining, TIMEOUT_LIMIT))
        try:
            data = sock.recv(chunk_size)
        except socket.timeout:
            if time.monotonic() - last_data_time >= TIMEOUT_LIMIT:
                break
            continue

        if not data:
            break

        chunks.append(data)
        last_data_time = time.monotonic()

    return b"".join(chunks)


def printable_ascii(data: bytes) -> str:
    try:
        text = data.decode("ascii")
    except UnicodeDecodeError:
        text = data.decode("ascii", errors="replace")
    return text.rstrip("\r")  # strip trailing CR sent by Cyclus2


class Cyclus2Session:
    """
    A TCP connection to the Cyclus2, modeled as a two-way conversation.
    send_line() sends a message to the Cyclus2; any text the Cyclus2 replies
    is delivered to a callback as soon as it arrives, whenever that is.
    A background thread does the actual socket reading, because the Cyclus2 does
    not always wait to be asked: For example, after command `data=7`,
    it keeps streaming data on its own.
    """

    def __init__(self, host: str, port: int, timeout: float = 2.0):
        self.timeout = timeout
        self.sock = socket.create_connection((host, port), timeout=timeout)
        self._on_message = lambda line: None
        self._running = True
        self._reader_thread = threading.Thread(target=self._read_loop, daemon=True)
        self._reader_thread.start()

    def set_message_handler(self, callback):
        """Register the function to call for every line received from the Cyclus2."""
        self._on_message = callback

    def _read_loop(self):
        while self._running:
            try:
                chunk = recv_stream(self.sock, timeout=self.timeout)
            except OSError:
                break  # the socket was closed, e.g. via close() below.

            for line in printable_ascii(chunk).splitlines():
                line = line.strip()
                if line:
                    self._on_message(line)

    def send_line(self, command: str):
        self.sock.sendall(command.encode("ascii") + REQUEST_NEWLINE)

    def close(self):
        self._running = False
        try:
            self.sock.shutdown(socket.SHUT_RDWR)
        except OSError:
            pass
        self.sock.close()


class ChatSession:
    """
    Runs the interactive chat: Everything the user sends and everything the
    Cyclus2 replies appears in the same scrolling transcript, with a single input
    line always available below it. The layout is directly adapted from
    prompt_toolkit's example calculator.py ("inspiration for a REPL"):
    A scrollable TextArea for the transcript, a one-line input TextArea below that,
    and a static horizontal line in between that visually separates the two,
    as part of the fixed screen layout.
    """

    def __init__(self, session: Cyclus2Session, command_catalog: dict):
        self.session = session
        self.command_catalog = command_catalog
        session.set_message_handler(self._on_device_message)

        intro = (ASCII_BANNER + "\n" +
                 "Type any Cyclus2 command or use HELP [command] for command reference.\n"
                 "To end the session, type DISCONNECT to disconnect from the Cyclus2.\n")
        self.log_area = TextArea(text=intro, read_only=True, wrap_lines=True, scrollbar=True)
        input_area = TextArea(height=1, prompt="Command> ", multiline=False, wrap_lines=False)
        input_area.accept_handler = self._on_submit

        layout = Layout(
            HSplit([self.log_area,
                    Window(height=1, char="─"),  # static separator, fixed in the layout
                    input_area]),
            focused_element=input_area,
        )

        bindings = KeyBindings()

        @bindings.add("c-c")
        def _quit(event):
            self.session.close()
            event.app.exit()

        self.app = Application(layout=layout, key_bindings=bindings, full_screen=True)

    def _append(self, line: str):
        # Keep the cursor at the end so the log area auto-scrolls down to the
        # newest line whenever it grows beyond the visible height.
        # NOTE: log_area is read_only, so writing its document needs
        # bypass_readonly=True; otherwise this silently raises
        # EditReadOnlyBuffer (caught by prompt_toolkit without a stack trace)
        # and neither the log update nor whatever runs after it takes effect.
        new_text = self.log_area.text + line + "\n"
        self.log_area.buffer.set_document(
            Document(new_text, cursor_position=len(new_text)),
            bypass_readonly=True)

    def _on_submit(self, buffer):
        text = buffer.text.strip()
        if not text:
            return

        self._append(f"\nCommand> {text}")

        if text == "DISCONNECT":
            self._append("Disconnecting and ending the session. Bye.")
            self.session.close()
            self.app.exit()
            return

        local_reply = local_reply_for(self.command_catalog, text)
        if local_reply is not None:
            self._append(local_reply)
            return

        self.session.send_line(text)

    def _on_device_message(self, text: str):
        self._append(f"Cyclus2> {text}")
        self.app.invalidate()  # invalidate() is documented as thread-safe.

    def run(self):
        self.app.run()


def parse_args():
    # NOTE: The initial prototype script only supports TCP/IP; the connection target
    #       is a network address. If serial support is added later, this could
    #       be separated into a --transport option (e.g., tcp | serial) with options
    #       --address and --device for each transport instead of reusing --address.
    parser = argparse.ArgumentParser(
        description="Interactively send commands to a Cyclus2 ergometer over TCP/IP."
    )
    parser.add_argument(
        "--address",
        default=None,
        help=f"IP address of your Cyclus2 ergometer (default: {DEFAULT_ADDRESS}).",
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
    return parser.parse_args()


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

    addr = args.address
    if addr is None:
        # If the address is not provided, prompt the user for it now.
        # For example, double-clicking the Windows executable will leave address unset.
        try:
            if sys.stdin.isatty():
                entered = input(f"Enter your Cyclus2 IP address [default is {DEFAULT_ADDRESS}]: ").strip()
                addr = entered or DEFAULT_ADDRESS
            else:
                addr = DEFAULT_ADDRESS
        except KeyboardInterrupt:
            print("\nReceived keyboard interrupt; aborting.")
            sys.exit(0)
        except EOFError:
            addr = DEFAULT_ADDRESS

    PORT = 25000  # default port 25000 on the Cyclus2 Ethernet/TCP interface  
    TIMEOUT_SOCKET = 2  # socket timeout in seconds for send/receive operations

    print(f"Trying to connect to {addr}:{PORT} ... ", end="", flush=True)

    try:
        session = Cyclus2Session(addr, PORT, timeout=TIMEOUT_SOCKET)
    except OSError as exc:
        print("connection failed :(.")  # complete above message "Trying to connect..."
        print("Please check the address; is the Cyclus2 reachable on the network?\n" +
              f"Connection error details: {exc}", file=sys.stderr)
        sys.exit(1)

    print("connection success :).")

    try:
        ChatSession(session, command_catalog).run()
    except KeyboardInterrupt:
        print("\nReceived keyboard interrupt; disconnecting.")
    except Exception as exc:
        print(f"ERROR: {exc}\n" +
              "Something went wrong with the script, see error above.\n" +
              "Ending the script now; try to restart it and/or report the error.",
              file=sys.stderr)
        sys.exit(1)
    finally:
        session.close()


if __name__ == "__main__":
    main()
