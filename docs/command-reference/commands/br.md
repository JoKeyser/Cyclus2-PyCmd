<!--
SPDX-FileCopyrightText: 2022 RBM elektronik-automation GmbH, Weissenfelser Strasse 73, 04229 Leipzig, Germany
SPDX-License-Identifier: NoAssertionLicense
SPDX-Description: Cyclus2 command reference entry derived from the Cyclus2 protocol specification PDF.
-->

---
command:
  name: br
  summary: Configuration of baud rate
  query:
    syntax: br?
    replies:
      ok: br:val
  configuration:
    syntax: br=val
    replies:
      ok: ok
      error: error:message
  parameters:
  - name: <val>
    type: unsigned short int
---

<!-- The YAML block above is machine-readable metadata; the Markdown below is for human-readable documentation. -->

br
===

Configuration of baud rate
--------------------------

Query command and replies
-------------------------

br? → br:`<val>`

Configuration command and replies
---------------------------------

br=`<val>` → ok or error:`<message>`

The response is sent with the so far preset baud rate.

Parameters
----------

`<val>` — baud rate.

Permitted presets are: 1200, 2400, 4800 (default), 9600, 19200, 38400, 56000, 57600, and 115200.

The 56000 setting does not exist any longer as from version 4, and the settings 57600 and 115200 are added instead.

The next command must be sent with the new baud rate.

Notes
-----

- Version 3.100
- Note: Changed in version 4
- Supported in release 5.0
