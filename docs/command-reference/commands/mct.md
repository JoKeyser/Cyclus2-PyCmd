<!--
SPDX-FileCopyrightText: 2022 RBM elektronik-automation GmbH, Weissenfelser Strasse 73, 04229 Leipzig, Germany
SPDX-License-Identifier: NoAssertionLicense
SPDX-Description: Cyclus2 command reference entry derived from the Cyclus2 protocol specification PDF.
-->

---
command:
  name: mct
  summary: Configuration of Maximum Cadence Test
  query:
    syntax: mct?
    replies:
      ok: mct:<val>[,<data>]
  configuration:
    syntax: mct=<val>,<data>
    replies:
      ok: ok
      error: error:<message>
  parameters:
  - name: val
    type: unsigned short int
    values:
    - code: 4
      meaning: Data <data> are available, Maximum Strength Test
    - code: else
      meaning: No parameter of Maximum Strength Test available
  - name: data
    type: sequence
    sequence:
    - name: LimitId
      type: unsigned short int
    - name: LimitValue
      type: float
    - name: InitialLoad
      type: float
    - name: HoldTime
      type: float
    - name: UnitId
      type: unsigned short int
---

<!-- The YAML block above is machine-readable metadata; the Markdown below is for human-readable documentation. -->

mct
===

Configuration of Maximum Cadence Test

Query command and replies
-------------------------

`mct?` 🡺 `mct:<val>[,data]`

Configuration command and replies
---------------------------------

`mct=<val>,<data>` 🡺 `ok` or `error:<message>`

(in slave mode only)

Parameters
----------

- `<val>` — Type of ergometry.
  - `4` — Data `<data>` are available, Maximum Strength Test.
  - `else` — No parameter of Maximum Strength Test available.
- `<data>` — Parameter of Maximum Strength Test with hold time.
  - `<LimitId>`,
  - `<LimitValue>`,
  - `<InitialLoad>`,
  - `<HoldTime>`,
  - `<UnitId>`

A description of the individual parameters is shown in chapter 2.4.
When writing, always set for `<val> = 4`.

Notes
-----

- Version 3.100
- Parameters must not be changed during a running training programme.
