<!--
SPDX-FileCopyrightText: 2022 RBM elektronik-automation GmbH, Weissenfelser Strasse 73, 04229 Leipzig, Germany
SPDX-License-Identifier: NoAssertionLicense
SPDX-Description: Cyclus2 command reference entry derived from the Cyclus2 protocol specification PDF.
-->

---
command:
  name: heap
  summary: Query of available heap size
  query:
    syntax: heap?
    replies:
      ok: heap:val
  parameters:
  - name: <val>
    type: float
---

<!-- The YAML block above is machine-readable metadata; the Markdown below is for human-readable documentation. -->

heap
====

Query of available heap size

Query command and replies
-------------------------

heap? → heap:`<val>`

Parameters
----------

`<val>` — Available heap size in bytes.

Notes
-----

- Version 3.100
- Supported in release 5.0
