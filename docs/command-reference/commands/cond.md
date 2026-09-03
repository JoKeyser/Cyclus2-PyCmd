<!--
SPDX-FileCopyrightText: 2022 RBM elektronik-automation GmbH, Weissenfelser Strasse 73, 04229 Leipzig, Germany
SPDX-License-Identifier: NoAssertionLicense
SPDX-Description: Cyclus2 command reference entry derived from the Cyclus2 protocol specification PDF.
-->

---
command:
  name: cond
  summary: Configuration of external field conditions
  query:
    syntax: cond?
    replies:
      ok: cond:data
  configuration:
    syntax: cond=data
    replies:
      ok: ok
      error: error:message
  parameters:
  - name: <data>
    type: sequence
    sequence:
    - name: <AirDensity>
      type: float
    - name: <RoadSurface>
      type: unsigned short int
      values:
      - code: '0'
        meaning: Paved road
      - code: '1'
        meaning: Asphaltic road
      - code: '2'
        meaning: Cement cycling track
      - code: '3'
        meaning: Wood cycling track
---

<!-- The YAML block above is machine-readable metadata; the Markdown below is for human-readable documentation. -->

cond
====

Configuration of external field conditions

Query command and replies
-------------------------

cond? → cond:`<data>`

Configuration command and replies
---------------------------------

cond=`<data>` → ok or error:`<message>`

Parameters
----------

`<data>` — Field parameter.

- `<AirDensity>`,
- `<RoadSurface>`,

`<RoadSurface>` — Road surface type.

- 0 — Paved road.
- 1 — Asphaltic road.
- 2 — Cement cycling track.
- 3 — Wood cycling track.

Notes
-----

- Version 3.100
- Parameters must not be changed during a running training programme.
