<!--
SPDX-FileCopyrightText: 2022 RBM elektronik-automation GmbH, Weissenfelser Strasse 73, 04229 Leipzig, Germany
SPDX-License-Identifier: NoAssertionLicense
SPDX-Description: Cyclus2 command reference entry derived from the Cyclus2 protocol specification PDF.
-->

---
command:
  name: temp
  summary: Query of motor temperature
  query:
    syntax: temp?
    replies:
      ok: temp:val
  parameters:
  - name: <val>
    type: float
---

<!-- The YAML block above is machine-readable metadata; the Markdown below is for human-readable documentation. -->

temp
====

Query of motor temperature

Query command and replies
-------------------------

temp? → temp:`<val>`

Parameters
----------

`<val>` — Temperature in °C.

Notes
-----

- Version 3.100
- Supported in release 5.0
