<!--
SPDX-FileCopyrightText: 2022 RBM elektronik-automation GmbH, Weissenfelser Strasse 73, 04229 Leipzig, Germany
SPDX-License-Identifier: NoAssertionLicense
SPDX-Description: Cyclus2 command reference entry derived from the Cyclus2 protocol specification PDF.
-->

---
command:
  name: os
  summary: Query of version of operating system
  query:
    syntax: os?
    replies:
      ok: os:val
  parameters:
  - name: <val>
    type: operating system version string
---

<!-- The YAML block above is machine-readable metadata; the Markdown below is for human-readable documentation. -->

os
===

Query of version of operating system

Query command and replies
-------------------------

os? → os:`<val>`

Parameters
----------

`<val>` — Version number in format `x.x.x.x`, Date + Time (e.g., `5.0.1.16, 30.06.2006 14:51:50,00`)

Notes
-----

- Version 4
- Supported in release 5.0
