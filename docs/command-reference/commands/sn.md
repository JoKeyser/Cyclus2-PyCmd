<!--
SPDX-FileCopyrightText: 2022 RBM elektronik-automation GmbH, Weissenfelser Strasse 73, 04229 Leipzig, Germany
SPDX-License-Identifier: NoAssertionLicense
SPDX-Description: Cyclus2 command reference entry derived from the Cyclus2 protocol specification PDF.
-->

---
command:
  name: sn
  summary: Query of serial number
  query:
    syntax: sn?
    replies:
      ok: sn:val
  parameters:
  - name: <val>
    type: serial number string
---

<!-- The YAML block above is machine-readable metadata; the Markdown below is for human-readable documentation. -->

sn
===

Query of serial number

Query command and replies
-------------------------

sn? → sn:`<val>`

Parameters
----------

`<val>` — Serial number in format dddd-ddddd-ddddd (e.g. 0297-10020-00046)

Notes
-----

- Version 3.100
- Supported in release 5.0
