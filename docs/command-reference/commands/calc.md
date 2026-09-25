<!--
SPDX-FileCopyrightText: 2022 RBM elektronik-automation GmbH, Weissenfelser Strasse 73, 04229 Leipzig, Germany
SPDX-License-Identifier: NoAssertionLicense
SPDX-Description: Cyclus2 command reference entry derived from the Cyclus2 protocol specification PDF.
-->

---
command:
  name: calc
  summary: Configuration of calculation parameter
  query:
    syntax: calc?
    replies:
      ok: calc:<interval>, <avg>
  configuration:
    syntax: calc=<interval>,<avg>
    replies:
      ok: ok
      error: error:<message>
  parameters:
  - name: interval
    type: unsigned short int
  - name: avg
    type: unsigned short int
---

<!-- The YAML block above is machine-readable metadata; the Markdown below is for human-readable documentation. -->

calc
====

Configuration of calculation parameter

Query command and replies
-------------------------

`calc?` 🡺 `calc:<interval>,<avg>`

Configuration command and replies
---------------------------------

`calc=<interval>,<avg>` 🡺 `ok` or `error:<message>`

(in slave mode only)

Parameters
----------

- `<interval>` — Minimum time in ms/10 (10..1000) between two data requests exchanged between control device and brake aggregate of the Cyclus2.
  For standard programmes the minimum time is always set to 500 ms `<interval>=50`.
  For the Maximum-Force-Test and Maximum-Cadence-Test it is always set to 250 ms `<interval>=25`.
- `<avg>` — Number of data sets (1..20).
  For the calculation of the floating mean value during the calculation of the training data on the Cyclus2.
  For standard programmes the parameter is always set to 10 data sets.
  For the tests, which respectively determine the Maximal Cadence and the Maximum Force `<avg> = 5`.

Notes
-----

- Version 3.100
- Note: as from version 4 no longer existent
