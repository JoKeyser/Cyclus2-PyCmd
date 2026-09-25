<!--
SPDX-FileCopyrightText: 2022 RBM elektronik-automation GmbH, Weissenfelser Strasse 73, 04229 Leipzig, Germany
SPDX-License-Identifier: NoAssertionLicense
SPDX-Description: Cyclus2 command reference entry derived from the Cyclus2 protocol specification PDF.
-->

---
command:
  name: rings
  summary: Configuration of the front chain rings for virtual gear shifting
  query:
    syntax: rings?
    replies:
      ok: rings:<data>
  configuration:
    syntax: rings=<data>
    replies:
      ok: ok
      error: error:<message>
  parameters:
  - name: data
    type: comma-separated sequence of variable length
---

<!-- The YAML block above is machine-readable metadata; the Markdown below is for human-readable documentation. -->

rings
=====

Configuration of the front chain rings for virtual gear shifting

Query command and replies
-------------------------

`rings?` 🡺 `rings:<data>`

Configuration command and replies
---------------------------------

`rings=<data>` 🡺 `ok` or `error:<message>`

(in slave mode only)

Parameters
----------

`<data>` — set chain rings separated by comma.

If no parameters are explicitly set, 0 will be rendered.
In this case, stepless gear shift is applied.
The number of parameters is variable.
The command `cycle` and `cycle1` delete the presets!

Example:

- `rings=0` (Settings will be deleted, stepless gear shift)
- `rings=39,53`

Notes
-----

- Version 4.2.4155
