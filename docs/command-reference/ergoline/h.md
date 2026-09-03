<!--
SPDX-FileCopyrightText: 2022 RBM elektronik-automation GmbH, Weissenfelser Strasse 73, 04229 Leipzig, Germany
SPDX-License-Identifier: NoAssertionLicense
SPDX-Description: Cyclus2 command reference entry derived from the Cyclus2 protocol specification PDF.
-->

---
command:
  name: h
  summary: Query of current heart rate
  query:
    syntax: h
    replies:
      ok: Hval
  parameters:
  - name: val
    type: unsigned short int
---

<!-- The YAML block above is machine-readable metadata; the Markdown below is for human-readable documentation. -->

h
===

Query of current heart rate

Query command and replies
-------------------------

`<h>` → H`<val>`

Parameters
----------
`<val>` — Current heart rate in bpm.

Notes
-----

- Version 2.200
- Supported in release 5.0
