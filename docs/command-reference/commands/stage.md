<!--
SPDX-FileCopyrightText: 2022 RBM elektronik-automation GmbH, Weissenfelser Strasse 73, 04229 Leipzig, Germany
SPDX-License-Identifier: NoAssertionLicense
SPDX-Description: Cyclus2 command reference entry derived from the Cyclus2 protocol specification PDF.
-->

---
command:
  name: stage
  summary: Configuration of load stages
  query:
    syntax: stage?
    replies:
      ok: stage:count
  configuration:
    syntax: stage=type[, data]
    replies:
      ok: ok
      error: error:message
  parameters:
  - name: <count>
    type: unsigned short int
  - name: <no>
    type: unsigned short int
  - name: <type>
    type: unsigned short int
    values:
    - code: '0'
      meaning: Existing programme will be deleted and the stages will be defined as
        first stage of the new programme
    - code: '1'
      meaning: Stage will be annexed to the programme
    - code: '2'
      meaning: Stage will be annexed to the programme and the programme preview is
        drawn
    - code: '3'
      meaning: No stage data; programme preview is drawn
  - name: <data>
    type: sequence
    sequence:
    - name: <Len>
      type: unsigned long
    - name: <Val1>
      type: float
    - name: <Val2>
      type: float
    - name: <StageType>
      type: unsigned short int
    - name: <ControlId>
      type: unsigned short int
    - name: <UnitId>
      type: unsigned short int
---

<!-- The YAML block above is machine-readable metadata; the Markdown below is for human-readable documentation. -->

stage
=====

Configuration of load stages

Query command and replies
-------------------------

stage? → stage:`<count>`

The query form stage?`<no>` returns stage:`<no>`, `<data>`.

Configuration command and replies
---------------------------------

stage=type[, data] → ok or error:`<message>`

Parameters
----------

`<count>` — Count of stages (30000..32000). To gain the number of stages, subtract 30000.

`<no>` — Index of stage (0..2000).

`<type>` — Defines the operation carried out with the data.

- 0 — Existing programme will be deleted and the stages will be defined as first stage of the new programme.
- 1 — Stage will be annexed to the programme.
- 2 — Stage will be annexed to the programme and the programme preview is drawn.
- 3 — No stage data; programme preview is drawn.

`<data>` — Parameter of stage.

- `<Len>`,
- `<Val1>`,
- `<Val2>`,
- `<StageType>`,
- `<ControlId>`,
- `<UnitId>`

Notes
-----

- Version 3.100
- Parameters must not be changed during a running training programme.
- Note: Changed in version 4; see chapter 2.2.
