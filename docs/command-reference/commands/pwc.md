<!--
SPDX-FileCopyrightText: 2022 RBM elektronik-automation GmbH, Weissenfelser Strasse 73, 04229 Leipzig, Germany
SPDX-License-Identifier: NoAssertionLicense
SPDX-Description: Cyclus2 command reference entry derived from the Cyclus2 protocol specification PDF.
-->

---
command:
  name: pwc
  summary: Configuration of the Power Warm-up Cycle
  query:
    syntax: pwc?
    replies:
      ok: pwc:val[,<data>]
  configuration:
    syntax: pwc=val,data
    replies:
      ok: ok
      error: error:message
  parameters:
  - name: <val>
    type: unsigned short int
    values:
    - code: '5'
      meaning: Data data are available, Power Warm-up Cycle
    - code: else
      meaning: No parameter of Power Warm-up Cycle available
  - name: <data>
    type: sequence
    sequence:
    - name: <LimitId>
      type: unsigned short int
    - name: <LimitValue>
      type: float
    - name: <InitialLoad>
      type: float
    - name: <UnitId>
      type: unsigned short int
    - name: <PWC>
      type: float
---

<!-- The YAML block above is machine-readable metadata; the Markdown below is for human-readable documentation. -->

pwc
===

Configuration of the Power Warm-up Cycle

Query command and replies
-------------------------

pwc? → pwc:`<val>`[,data]

Configuration command and replies
---------------------------------

pwc=`<val>`,`<data>` → ok or error:`<message>`

Parameters
----------

`<val>` — Type of ergometry.

- 5 — Data `<data>` are available, Power Warm-up Cycle.
- else — No parameter of Power Warm-up Cycle available.

`<data>` — Parameter of Power Warm-up Cycle.

- `<LimitId>`,
- `<LimitValue>`,
- `<InitialLoad>`,
- `<UnitId>`,
- `<PWC>`,

Notes
-----

- Version 3.100
- Parameters must not be changed during a running training programme.
- The PWC value is defined via this command.
