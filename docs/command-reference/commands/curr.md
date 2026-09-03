<!--
SPDX-FileCopyrightText: 2022 RBM elektronik-automation GmbH, Weissenfelser Strasse 73, 04229 Leipzig, Germany
SPDX-License-Identifier: NoAssertionLicense
SPDX-Description: Cyclus2 command reference entry derived from the Cyclus2 protocol specification PDF.
-->

---
command:
  name: curr
  summary: Query of motor current
  query:
    syntax: curr?
    replies:
      ok: curr:val
  parameters:
  - name: <val>
    type: float
---

<!-- The YAML block above is machine-readable metadata; the Markdown below is for human-readable documentation. -->

curr
====

Query of motor current

Query command and replies
-------------------------

curr? → curr:`<val>`

Parameters
----------

`<val>` — Current in amperes.

Notes
-----

- Version 3.100
- Supported in release 5.0
