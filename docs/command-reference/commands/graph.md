<!--
SPDX-FileCopyrightText: 2022 RBM elektronik-automation GmbH, Weissenfelser Strasse 73, 04229 Leipzig, Germany
SPDX-License-Identifier: NoAssertionLicense
SPDX-Description: Cyclus2 command reference entry derived from the Cyclus2 protocol specification PDF.
-->

---
command:
  name: graph
  summary: Configuration of chart
  query:
    syntax: graph?
    replies:
      ok: graph:data
  configuration:
    syntax: graph=data
    replies:
      ok: ok
      error: error:message
  parameters:
  - name: data
    type: sequence
    sequence:
    - name: XId
      type: unsigned short int
    - name: XStart
      type: float
    - name: XRange
      type: float
    - name: LeftId
      type: unsigned short int
    - name: LeftStart
      type: float
    - name: LeftRange
      type: float
    - name: RightId
      type: unsigned short int
    - name: RightStart
      type: float
    - name: RightRange
      type: float
    - name: WithGrid
      type: unsigned short int
---

<!-- The YAML block above is machine-readable metadata; the Markdown below is for human-readable documentation. -->

graph
=====

Configuration of chart

Query command and replies
-------------------------

graph? → graph:`<data>`

Configuration command and replies
---------------------------------

graph=`<data>` → ok or error:`<message>`

Parameters
----------

`<data>` — Parameter of chart.

- `<XId>`,
- `<XStart>`,
- `<XRange>`,
- `<LeftId>`,
- `<LeftStart>`,
- `<LeftRange>`,
- `<RightId>`,
- `<RightStart>`,
- `<RightRange>`,
- `<WithGrid>`

Notes
-----

- Version 3.100
- Parameters must not be changed during a running training programme.
