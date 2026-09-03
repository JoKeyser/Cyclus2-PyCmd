<!--
SPDX-FileCopyrightText: 2022 RBM elektronik-automation GmbH, Weissenfelser Strasse 73, 04229 Leipzig, Germany
SPDX-License-Identifier: NoAssertionLicense
SPDX-Description: Cyclus2 command reference entry derived from the Cyclus2 protocol specification PDF.
-->

---
command:
  name: b
  summary: Query of current power
  query:
    syntax: b
    replies:
      ok: Bval
  parameters:
  - name: val
    type: unsigned short int
---

<!-- The YAML block above is machine-readable metadata; the Markdown below is for human-readable documentation. -->

b
===

Query of current power

Query command and replies
-------------------------

`<b>` → B`<val>`

Parameters
----------

`<val>` — Current power in watts.

Notes
-----

- Version 2.200
- Supported in release 5.0
