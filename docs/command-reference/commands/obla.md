<!--
SPDX-FileCopyrightText: 2022 RBM elektronik-automation GmbH, Weissenfelser Strasse 73, 04229 Leipzig, Germany
SPDX-License-Identifier: NoAssertionLicense
SPDX-Description: Cyclus2 command reference entry derived from the Cyclus2 protocol specification PDF.
-->

---
command:
  name: obla
  summary: Configuration of the OBLA threshold test
  query:
    syntax: obla?
    replies:
      ok: obla:val[,<data>]
  configuration:
    syntax: obla=val,data
    replies:
      ok: ok
      error: error:message
  parameters:
  - name: <val>
    type: unsigned short int
    values:
    - code: '5'
      meaning: Data data are available, OBLA threshold test
    - code: else
      meaning: No parameter of OBLA available
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
    - name: <OBLA>
      type: float
---

<!-- The YAML block above is machine-readable metadata; the Markdown below is for human-readable documentation. -->

obla
====

Configuration of the OBLA threshold test

Query command and replies
-------------------------

obla? → obla:`<val>`[,data]

Configuration command and replies
---------------------------------

obla=`<val>`,`<data>` → ok or error:`<message>`

Parameters
----------

`<val>` — Type of ergometry.

- 5 — Data `<data>` are available, OBLA threshold test.
- else — No parameter of OBLA available.

`<data>` — Parameter of OBLA.

- `<LimitId>`,
- `<LimitValue>`,
- `<InitialLoad>`,
- `<UnitId>`,
- `<OBLA>`

Notes
-----

- Version 3.100
- Parameters must not be changed during a running training programme.
- This command defines the threshold used for the OBLA test.
