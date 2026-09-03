<!--
SPDX-FileCopyrightText: 2022 RBM elektronik-automation GmbH, Weissenfelser Strasse 73, 04229 Leipzig, Germany
SPDX-License-Identifier: NoAssertionLicense
SPDX-Description: Cyclus2 command reference entry derived from the Cyclus2 protocol specification PDF.
-->

---
command:
  name: jump
  summary: Jump to a load stage
  query:
    syntax: jump?
    replies:
      ok: jump:val
  configuration:
    syntax: jump=val
    replies:
      ok: ok
      error: error:message
  parameters:
  - name: <val>
    type: unsigned short int
---

<!-- The YAML block above is machine-readable metadata; the Markdown below is for human-readable documentation. -->

jump
====

Jump to a load stage

Query command and replies
-------------------------

jump? → jump:`<val>`

Configuration command and replies
---------------------------------

jump=`<val>` → ok or error:`<message>`

Parameters
----------

`<val>` — Number of load stage, from 1 to `<n>`.

Notes
-----

- Supported in release 5.0
