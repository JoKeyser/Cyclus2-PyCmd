<!--
SPDX-FileCopyrightText: 2022 RBM elektronik-automation GmbH, Weissenfelser Strasse 73, 04229 Leipzig, Germany
SPDX-License-Identifier: NoAssertionLicense
SPDX-Description: Cyclus2 command reference entry derived from the Cyclus2 protocol specification PDF.
-->

---
command:
  name: cassette
  summary: Configuration of the cassette with the available rear sprockets for virtual
    gear shifting
  query:
    syntax: cassette?
    replies:
      ok: cassette:data
  configuration:
    syntax: cassette=data
    replies:
      ok: ok
      error: error:message
  parameters:
  - name: <data>
    type: sequence of unsigned short int
---

<!-- The YAML block above is machine-readable metadata; the Markdown below is for human-readable documentation. -->

cassette
========

Configuration of the cassette with the available rear sprockets for virtual gear shifting

Query command and replies
-------------------------

cassette? → cassette:`<data>`

Configuration command and replies
---------------------------------

cassette=`<data>` → ok or error:`<message>`

Parameters
----------

`<data>` — Preset sprockets separated by commas.

- `<rear sprocket 1>`,
- `<rear sprocket 2>`,
- ...

If no parameters have been explicitly set, 0 is rendered. In this case stepless gear shift is applied. The number of parameters is variable. The command `<cycle>` and `<cycle1>` delete the presets.

Examples:

- cassette=0 (presets will be deleted, stepless gear shift)
- cassette=12,13,14,15,16,17,19,21,23,25

Notes
-----

- Version 4.2.4155
