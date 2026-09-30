<!--
SPDX-FileCopyrightText: 2022 RBM elektronik-automation GmbH, Weissenfelser Strasse 73, 04229 Leipzig, Germany
SPDX-License-Identifier: NoAssertionLicense
SPDX-Description: Cyclus2 command reference entry derived from the Cyclus2 protocol specification PDF.
-->

---
command:
  name: "w"
  summary: "Set the target value during exercise"
  configuration:
    syntax: "w<val>"
    replies:
      ok: NONE
  parameters:
  - name: "val"
    type: "unsigned short int"
---

<!-- The YAML block above is machine-readable metadata; the Markdown below is for human-readable documentation. -->

w
===

Set the target value during exercise

Configuration command
--------------------

`w<val>`

(in slave mode only)

Parameters
----------

`<val>` — Target value (0..2000 Watts)

Notes
-----

- Version 2.200
- Supported in release 5.0
