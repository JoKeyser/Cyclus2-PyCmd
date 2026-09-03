<!--
SPDX-FileCopyrightText: 2022 RBM elektronik-automation GmbH, Weissenfelser Strasse 73, 04229 Leipzig, Germany
SPDX-License-Identifier: NoAssertionLicense
SPDX-Description: Cyclus2 command reference entry derived from the Cyclus2 protocol specification PDF.
-->

---
command:
  name: want
  summary: Configuration of the threshold of the WAnT test
  query:
    syntax: want?
    replies:
      ok: want:val[,<data>]
  configuration:
    syntax: want=val,data
    replies:
      ok: ok
      error: error:message
  parameters:
  - name: <val>
    type: unsigned short int
    values:
    - code: '5'
      meaning: Data data are available, WAnT test
    - code: else
      meaning: No parameter of WAnT available
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
    - name: <Threshold>
      type: float
---

<!-- The YAML block above is machine-readable metadata; the Markdown below is for human-readable documentation. -->

want
====

Configuration of the threshold of the WAnT test

Query command and replies
-------------------------

want? → want:`<val>`[,data]

Configuration command and replies
---------------------------------

want=`<val>`,`<data>` → ok or error:`<message>`

Parameters
----------

`<val>` — Type of ergometry.

- 5 — Data `<data>` are available, WAnT test.
- else — No parameter of WAnT available.

`<data>` — Parameter of WAnT.

- `<LimitId>`,
- `<LimitValue>`,
- `<InitialLoad>`,
- `<UnitId>`,
- `<Threshold>`,

Notes
-----

- Version 3.100
- Parameters must not be changed during a running training programme.
- In case of WAnT testing, the threshold is set with this command.
