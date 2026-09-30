<!--
SPDX-FileCopyrightText: 2022 RBM elektronik-automation GmbH, Weissenfelser Strasse 73, 04229 Leipzig, Germany
SPDX-License-Identifier: NoAssertionLicense
SPDX-Description: Cyclus2 command reference entry derived from the Cyclus2 protocol specification PDF.
-->

---
command:
  name: "check"
  summary: "Configuration of monitoring (cf. mon)"
  query:
    syntax: "check?"
    replies:
      ok: "check:<Id-Flags>"
  configuration:
    syntax: "check=<Id>,<Min>,<Max>"
    replies:
      ok: "ok"
      error: "error:<message>"
  parameters:
  - name: "Id-Flags"
    type: "unsigned short int"
  - name: "Id"
    type: "unsigned short int"
  - name: "Min"
    type: "float"
  - name: "Max"
    type: "float"
---

<!-- The YAML block above is machine-readable metadata; the Markdown below is for human-readable documentation. -->

check
=====

Configuration of monitoring (cf. `mon`)

Query command and replies
-------------------------

`check?` 🡺 `check:<Id-Flags>`

`check?<Id>` 🡺 `check:<Id>,<Min>,<Max>`

Configuration command and replies
---------------------------------

`check=<Id>,<Min>,<Max>` 🡺 `ok` or `error:<message>`

(in slave mode only)

Parameters
----------

- `<Id-Flags>` — Flags of available monitoring items.
  The output is in hexadecimal format.
  For better distinction the flag `0x8000` is additionally set.
- `<Id>` — Identifier of the monitoring item
- `<Min>` — Lower limit of the training range
- `<Max>` — Upper limit of the training range

A description of the flags and IDs is shown in chapter 2.1.
The unit for the parameters `<Min>` and `<Max>` is also documented there.
If a monitoring is to be deleted, both parameters, `<Min>` and `<Max>`, must be set to `0`.

Notes
-----

- Version 3.100
- In addition to that, the command `<mon>` is available as from version 4.
