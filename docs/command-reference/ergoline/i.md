<!--
SPDX-FileCopyrightText: 2022 RBM elektronik-automation GmbH, Weissenfelser Strasse 73, 04229 Leipzig, Germany
SPDX-License-Identifier: NoAssertionLicense
SPDX-Description: Cyclus2 command reference entry derived from the Cyclus2 protocol specification PDF.
-->

---
command:
  name: i
  summary: Query of device id
  query:
    syntax: i
    replies:
      ok: er800P10V243
---

<!-- The YAML block above is machine-readable metadata; the Markdown below is for human-readable documentation. -->

i
===

Query of device id

Query command and replies
-------------------------

`<i>` → `<er800P10V243>`

Notes
-----

- Version 2.200
- Note: Changed in version 4; the reply is equivalent to the Ergoline 800 software version 2.9.
- Supported in release 5.0
