#!/usr/bin/env python3
#
# PURPOSE: Prototype of an interactive command-line interface to Cyclus2.
# AUTHORS: Johannes Keyser <johannes.keyser@uni-hamburg.de>
# LICENSE: EUPL-1.2
# SUMMARY: This script connects to a Cyclus2 ergometer over TCP/IP and
#          allows the user to interactively type commands like "data?".
#          It assumes that the Cyclus2 server is running and accessible
#          at the specified HOST and PORT, see code below.
#
# SPDX-FileCopyrightText: Johannes Keyser <johannes.keyser@uni-hamburg.de>
# SPDX-License-Identifier: EUPL-1.2

import argparse
import socket
import sys
import time

# Cyclus2 uses ASCII commands and a CRLF terminator on requests.
# Responses are plain ASCII and end with CR, with no trailing LF.
REQUEST_NEWLINE = b"\r\n"


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


def send_and_receive_ascii(sock, command: str, timeout: float):
    payload = command.encode("ascii") + REQUEST_NEWLINE
    sock.sendall(payload)

    response = recv_stream(sock, timeout=timeout)
    if not response:
        print("<no response from Cyclus2>")
        return response

    print(printable_ascii(response) + "\n")
    return response


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
        default="192.168.1.200",
        help="IP address of your Cyclus2 ergometer (default: %(default)s).",
    )
    return parser.parse_args()


def main():
    args = parse_args()
    addr = args.address
    PORT = 25000  # default port 25000 on the Cyclus2 Ethernet/TCP interface  
    TIMEOUT_SOCKET = 2  # socket timeout in seconds for send/receive operations

    try:
        with socket.create_connection((addr, PORT), timeout=TIMEOUT_SOCKET) as sock:
            print(f"Connected to {addr}:{PORT}, assuming it is a Cyclus2 ergometer.")
            print("Type any Cyclus2 command or type `quit` or `exit` to end the session.")
            print("For example, try `vers?` and press <Return> for the software version.\n")

            while True:
                try:
                    user_input = input("> ")
                except EOFError:
                    print("\nEOF received, ending the session.")
                    break

                if not user_input:
                    print("\nNo command received; type a Cyclus2 command or `quit`/`exit` to stop.")
                    continue
                if user_input.lower() in {"quit", "exit"}:
                    print("Closing the connection to the Cyclus2 ergometer.")
                    break

                send_and_receive_ascii(sock, user_input, timeout=TIMEOUT_SOCKET)

    except KeyboardInterrupt:
        print("\nReceived keyboard interrupt (Ctrl+C); closing the connection.")
        sys.exit(0)
    except OSError as exc:
        print(f"Could not connect to {addr} at port {PORT}.", file=sys.stderr)
        print("Please check the address; is the Cyclus2 reachable on the network?", file=sys.stderr)
        print(f"Connection error details: {exc}", file=sys.stderr)
        sys.exit(1)
    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        print("Something went wrong with the script, see error above.", file=sys.stderr)
        print("Ending the script now; try to restart it and/or report the error.", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
