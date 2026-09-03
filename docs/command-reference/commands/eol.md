<!--
SPDX-FileCopyrightText: 2022 RBM elektronik-automation GmbH, Weissenfelser Strasse 73, 04229 Leipzig, Germany
SPDX-License-Identifier: NoAssertionLicense
SPDX-Description: Cyclus2 command reference entry derived from the Cyclus2 protocol specification PDF.
-->

---
command:
  name: eol
  summary: Configuration of the end of line
  query:
    syntax: eol?
    replies:
      ok: eol:<val1>,val2
  configuration:
    syntax: eol=val1,val2
    replies:
      ok: ok
      error: error:message
  parameters:
  - name: <val1>
    type: char
  - name: <val2>
    type: char
---

<!-- The YAML block above is machine-readable metadata; the Markdown below is for human-readable documentation. -->

eol
===

Configuration of the end of line

Query command and replies
-------------------------

eol? → eol:`<val1>`,`<val2>`

Configuration command and replies
---------------------------------

eol=`<val1>`,`<val2>` → ok or error:`<message>`

Parameters
----------

`<val1>` — 1. character. 13 only is accepted for `<CR>`.

`<val2>` — 2. character. Possible settings are 0 (no second character) and 10 for `<LF>`.

Notes
-----

- Version 3.100
- Supported in release 5.0
