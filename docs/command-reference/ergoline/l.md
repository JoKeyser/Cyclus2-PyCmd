<!--
SPDX-FileCopyrightText: 2022 RBM elektronik-automation GmbH, Weissenfelser Strasse 73, 04229 Leipzig, Germany
SPDX-License-Identifier: NoAssertionLicense
SPDX-Description: Cyclus2 command reference entry derived from the Cyclus2 protocol specification PDF.
-->

---
command:
  name: l
  summary: Set load changes in time interval
  configuration:
    syntax: lval
    replies:
      ok: no reply
  parameters:
  - name: val
    type: unsigned short int
---

<!-- The YAML block above is machine-readable metadata; the Markdown below is for human-readable documentation. -->

l
===

Set load changes in time interval

Configuration command
--------------------

l`<val>`

Parameters
----------
`<val>` — Load changes per minute in watts, range 0..1000.

Notes
-----

- Version 2.200
- Supported in release 5.0
- Reset after commands `<w>` or `<f>`.
- Only valid in slave mode.
