<!--
SPDX-FileCopyrightText: 2022 RBM elektronik-automation GmbH, Weissenfelser Strasse 73, 04229 Leipzig, Germany
SPDX-License-Identifier: NoAssertionLicense
SPDX-Description: Cyclus2 command reference entry derived from the Cyclus2 protocol specification PDF.
-->

---
command:
  name: gen
  summary: Configuration of ergometry loads with the load generator
  query:
    syntax: gen?
    replies:
      ok: gen:val[,<data>]
  configuration:
    syntax: gen=val,data
    replies:
      ok: ok
      error: error:message
  parameters:
  - name: <val>
    type: unsigned short int
    values:
    - code: '8'
      meaning: Data data are available, source is load generator
    - code: '9'
      meaning: Data data are available, source is Conconi Test
    - code: '10'
      meaning: Data data are available, source are OBLA test
    - code: else
      meaning: No parameter of generator available
  - name: <data>
    type: sequence
    sequence:
    - name: <Len1>
      type: unsigned long
    - name: <Len2>
      type: unsigned long
    - name: <Len3>
      type: unsigned long
    - name: <Len4>
      type: unsigned long
    - name: <BasicLoad>
      type: float
    - name: <Plateau1>
      type: float
    - name: <Modification>
      type: float
    - name: <TypeOfCyclus>
      type: unsigned short int
    - name: <TypeOfLoad>
      type: unsigned short int
    - name: <TypeOfLen>
      type: unsigned short int
    - name: <Repetitions>
      type: unsigned short int
---

<!-- The YAML block above is machine-readable metadata; the Markdown below is for human-readable documentation. -->

gen
===

Configuration of ergometry loads with the load generator

Query command and replies
-------------------------

gen? → gen:`<val>`[,data]

Configuration command and replies
---------------------------------

gen=`<val>`,`<data>` → ok or error:`<message>`

Parameters
----------

`<val>` — Type of generator ergometry loads.

- 8 — Data `<data>` are available; source is load generator.
- 9 — Data `<data>` are available; source is Conconi Test.
- 10 — Data `<data>` are available; source are OBLA test.
- else — No parameter of generator available.

`<data>` — Parameter of generator.

- `<Len1>`,
- `<Len2>`,
- `<Len3>`,
- `<Len4>`,
- `<BasicLoad>`,
- `<Plateau1>`,
- `<Modification>`,
- `<TypeOfCyclus>`,
- `<TypeOfLoad>`,
- `<TypeOfLen>`,
- `<Repetitions>`

Notes
-----

- Version 3.100
- Parameters must not be changed during a running training programme.
- When generating, always use `<val>` = 8.
