<!--
SPDX-FileCopyrightText: 2022 RBM elektronik-automation GmbH, Weissenfelser Strasse 73, 04229 Leipzig, Germany
SPDX-License-Identifier: NoAssertionLicense
SPDX-Description: Cyclus2 command reference entry derived from the Cyclus2 protocol specification PDF.
-->

---
command:
  name: mpt
  summary: Configuration of Maximum Strength Test
  query:
    syntax: mpt?
    replies:
      ok: mpt:val[,<data>]
  configuration:
    syntax: mpt=val,data
    replies:
      ok: ok
      error: error:message
  parameters:
  - name: <val>
    type: unsigned short int
    values:
    - code: '5'
      meaning: Data data are available, Maximum Strength Test
    - code: else
      meaning: No parameter of Maximum Strength Test available
  - name: <data>
    type: sequence
    sequence:
    - name: <LimitId>
      type: unsigned short int
    - name: <LimitValue>
      type: float
    - name: <InitialLoad>
      type: float
    - name: <Len>
      type: unsigned long
    - name: <UnitId>
      type: unsigned short int
    - name: <StartValue>
      type: float
---

<!-- The YAML block above is machine-readable metadata; the Markdown below is for human-readable documentation. -->

mpt
===

Configuration of Maximum Strength Test

Query command and replies
-------------------------

mpt? → mpt:`<val>`[,data]

Configuration command and replies
---------------------------------

mpt=`<val>`,`<data>` → ok or error:`<message>`

Parameters
----------

`<val>` — Type of ergometry.

- 5 — Data `<data>` are available, Maximum Strength Test.
- else — No parameter of Maximum Strength Test available.

`<data>` — Parameter of Maximum Strength Test.

- `<LimitId>`,
- `<LimitValue>`,
- `<InitialLoad>`,
- `<Len>`,
- `<UnitId>`,
- `<StartValue>`,

Notes
-----

- Version 3.100
- Parameters must not be changed during a running training programme.
- Note: Changed in version 4; see chapter 2.4.
- When writing, always set `<val>` = 5.
