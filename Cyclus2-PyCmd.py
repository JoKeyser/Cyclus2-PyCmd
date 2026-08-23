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
    TIMEOUT_LIMIT = 0.25  # seconds of idle time to consider the stream finished

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
        print("<no response>")
        return response

    print(printable_ascii(response))
    return response


def main():
    # Settings worked for initial test; TODO: Make Host IP configurable.
    HOST = "192.168.1.200"
    PORT = 25000  # Cyclus2 default port is 25000
    TIMEOUT = 2

    try:
        with socket.create_connection((HOST, PORT), timeout=TIMEOUT) as s:
            print(f"Connected to {HOST}:{PORT}")
            print("ASCII protocol assumed: CRLF command terminator, plain ASCII response.")

            while True:
                try:
                    cmd = input("> ")
                except EOFError:
                    print("\nEOF received, exiting.")
                    break

                if not cmd:
                    continue
                if cmd.lower() in {"quit", "exit"}:
                    break

                send_and_receive_ascii(s, cmd, timeout=TIMEOUT)

    except KeyboardInterrupt:
        print("\nInterrupted.")
    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
