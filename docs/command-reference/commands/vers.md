<!--
SPDX-FileCopyrightText: 2022 RBM elektronik-automation GmbH, Weissenfelser Strasse 73, 04229 Leipzig, Germany
SPDX-License-Identifier: NoAssertionLicense
SPDX-Description: Cyclus2 command reference entry derived from the Cyclus2 protocol specification PDF.
-->

---
command:
  name: vers
  summary: Query of software version
  query:
    syntax: vers?
    replies:
      ok: 'vers: Cyclus2, Version val'
  parameters:
  - name: <val>
    type: version string
---

<!-- The YAML block above is machine-readable metadata; the Markdown below is for human-readable documentation. -->

vers
====

Query of software version

Query command and replies
-------------------------

vers? → vers: Cyclus2, Version `<val>`

Parameters
----------

`<val>` — Version number in format `d.ddd` (e.g., `3.100`) or from Version 4 in format `d.d.d.d` (e.g., `4.0.2392.23489`)

Notes
-----

- Version 3.100
- Note: Changed in version 4
- Supported in release 5.0
