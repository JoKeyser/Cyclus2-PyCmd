<!--
SPDX-FileCopyrightText: 2022 RBM elektronik-automation GmbH, Weissenfelser Strasse 73, 04229 Leipzig, Germany
SPDX-License-Identifier: NoAssertionLicense
SPDX-Description: Cyclus2 command reference entry derived from the Cyclus2 protocol specification PDF.
-->

---
command:
  name: w
  summary: Set the target value during exercise
  configuration:
    syntax: wval
    replies:
      ok: no reply
  parameters:
  - name: val
    type: unsigned short int
---

<!-- The YAML block above is machine-readable metadata; the Markdown below is for human-readable documentation. -->

w
===

Set the target value during exercise

Configuration command
--------------------

w`<val>`

Parameters
----------
`<val>` — Target value in watts, range 0..2000.

Notes
-----

- Version 2.200
- Supported in release 5.0
- Only valid in slave mode.
