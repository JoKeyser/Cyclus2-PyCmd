<!--
SPDX-FileCopyrightText: 2022 RBM elektronik-automation GmbH, Weissenfelser Strasse 73, 04229 Leipzig, Germany
SPDX-License-Identifier: NoAssertionLicense
SPDX-Description: Cyclus2 command reference entry derived from the Cyclus2 protocol specification PDF.
-->

---
command:
  name: "graph"
  summary: "Configuration of chart"
  query:
    syntax: "graph?"
    replies:
      ok: "graph:<data>"
  configuration:
    syntax: "graph=<data>"
    replies:
      ok: "ok"
      error: "error:<message>"
  parameters:
  - name: "data"
    type: "sequence"
    sequence:
    - name: "XId"
      type: "unsigned short int"
    - name: "XStart"
      type: "float"
    - name: "XRange"
      type: "float"
    - name: "LeftId"
      type: "unsigned short int"
    - name: "LeftStart"
      type: "float"
    - name: "LeftRange"
      type: "float"
    - name: "RightId"
      type: "unsigned short int"
    - name: "RightStart"
      type: "float"
    - name: "RightRange"
      type: "float"
    - name: "WithGrid"
      type: "unsigned short int"
---

<!-- The YAML block above is machine-readable metadata; the Markdown below is for human-readable documentation. -->

graph
=====

Configuration of chart

Query command and replies
-------------------------

`graph?` 🡺 `graph:<data>`

Configuration command and replies
---------------------------------

`graph=<data>` 🡺 `ok` or `error:<message>`

(in slave mode only)

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

The unit of the x-axis is defined by the parameter `XId`; `XStart` and `XRange` define the absolute values in relation to the unit.
For further information, please refer to the paragraph length type in chapter 2.1.
On the Cyclus2, two training parameters can be simultaneously graphically analysed, left and right.
The respective parameters `LeftId` and `RightId` define the training factor whereas the unit as well as the parameters `LeftStart`, `LeftRange` and `RightStart`, `RightRange` define the absolute values thereof, respectively.
The parameter `WithGrid` sets the display of the auxiliary grid in the diagram.

Notes
-----

- Version 3.100
- Parameters must not be changed during a running training programme.
