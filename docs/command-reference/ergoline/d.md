<!--
SPDX-FileCopyrightText: 2022 RBM elektronik-automation GmbH, Weissenfelser Strasse 73, 04229 Leipzig, Germany
SPDX-License-Identifier: NoAssertionLicense
SPDX-Description: Cyclus2 command reference entry derived from the Cyclus2 protocol specification PDF.
-->

---
command:
  name: d
  summary: Query of current cadence
  query:
    syntax: d
    replies:
      ok: nval
  parameters:
  - name: val
    type: unsigned short int
---

<!-- The YAML block above is machine-readable metadata; the Markdown below is for human-readable documentation. -->

d
===

Query of current cadence

Query command and replies
-------------------------

`<d>` → n`<val>`

Parameters
----------
`<val>` — Current cadence in rpm.

Notes
-----

- Version 2.200
- Supported in release 5.0
