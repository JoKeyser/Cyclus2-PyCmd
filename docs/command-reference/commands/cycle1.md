<!--
SPDX-FileCopyrightText: 2022 RBM elektronik-automation GmbH, Weissenfelser Strasse 73, 04229 Leipzig, Germany
SPDX-License-Identifier: NoAssertionLicense
SPDX-Description: Cyclus2 command reference entry derived from the Cyclus2 protocol specification PDF.
-->

---
command:
  name: cycle1
  summary: Configuration of the mounted bike (new version)
  query:
    syntax: cycle1?
    replies:
      ok: cycle1:data
  configuration:
    syntax: cycle1=data
    replies:
      ok: ok
      error: error:message
  parameters:
  - name: <data>
    type: sequence
    sequence:
    - name: Version for later extensions, 0 for the structure below
      type: unsigned short int
    - name: <Wheel size in Meters>
      type: float
    - name: <Crank length in Meters>
      type: float
    - name: <Weight in Kilogramms>
      type: float
    - name: <Real front chain ring>
      type: unsigned short int
    - name: <Real rear sprocket>
      type: unsigned short int
    - name: <Virtual front chain ring>
      type: unsigned short int
    - name: <Virtual rear sprocket>
      type: unsigned short int
---

<!-- The YAML block above is machine-readable metadata; the Markdown below is for human-readable documentation. -->

cycle1
======

Configuration of the mounted bike (new version)

Query command and replies
-------------------------

cycle1? → cycle1:`<data>`

Configuration command and replies
---------------------------------

cycle1=`<data>` → ok or error:`<message>`

Parameters
----------

`<data>` — Comma-separated parameter list for the mounted bike.

- `<Version for later extensions, 0 for the structure below>`,
- `<Wheel size in Meters>`,
- `<Crank length in Meters>`,
- `<Weight in Kilogramms>`,
- `<Real front chain ring>`,
- `<Real rear sprocket>`,
- `<Virtual front chain ring>`,
- `<Virtual rear sprocket>`,

Notes
-----

- Version 4.2.4155, new version for Cycle
