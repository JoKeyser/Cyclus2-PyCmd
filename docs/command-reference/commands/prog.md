<!--
SPDX-FileCopyrightText: 2022 RBM elektronik-automation GmbH, Weissenfelser Strasse 73, 04229 Leipzig, Germany
SPDX-License-Identifier: NoAssertionLicense
SPDX-Description: Cyclus2 command reference entry derived from the Cyclus2 protocol specification PDF.
-->

---
command:
  name: "prog"
  summary: "Query of the current type of ergometry"
  query:
    syntax: "prog?"
    replies:
      ok: "prog:<val>"
  parameters:
  - name: "val"
    type: "unsigned short int"
    values:
    - code: 0
      meaning: "manual control, without control of load duration"
    - code: 1
      meaning: "ergometry with some stages"
    - code: 4
      meaning: "Maximum Cadence Test"
    - code: 5
      meaning: "Maximum Strength Test"
    - code: 8
      meaning: "Source of ergometry is the load generator"
    - code: 9
      meaning: "Conconi Test"
    - code: 10
      meaning: "OBLA Test"
    - code: 11
      meaning: "Slave mode without control of the duration"
    - code: 12
      meaning: "Wingate Anaerobic Test"
    - code: 13
      meaning: "PWC Test"
    - code: 14
      meaning: "Real life track"
---

<!-- The YAML block above is machine-readable metadata; the Markdown below is for human-readable documentation. -->

prog
====

Query of the current type of ergometry

Query command and replies
-------------------------

`prog?` 🡺 `prog:<val>`

Parameters
----------

`<val>` — Current ergometry program type.

- `0` — manual control, without control of load duration
- `1` — ergometry with some stages
- `4` — Maximum Cadence Test
- `5` — Maximum Strength Test
- `8` — Source of ergometry is the load generator
- `9` — Conconi Test
- `10` — OBLA Test
- `11` — Slave mode without control of the duration

new with version 4

- `12` — Wingate Anaerobic Test
- `13` — PWC Test
- `14` — Real life track

Notes
-----

- Version 3.100
- Note: Changed in version 4
