<!--
SPDX-FileCopyrightText: 2022 RBM elektronik-automation GmbH, Weissenfelser Strasse 73, 04229 Leipzig, Germany
SPDX-License-Identifier: NoAssertionLicense
SPDX-Description: Cyclus2 command reference entry derived from the Cyclus2 protocol specification PDF.
-->

---
command:
  name: cycle
  summary: Configuration of the mounted bike
  query:
    syntax: cycle?
    replies:
      ok: cycle:data
  configuration:
    syntax: cycle=data
    replies:
      ok: ok
      error: error:message
  parameters:
  - name: <data>
    type: sequence
    sequence:
    - name: <wheel size in Meters>
      type: float
    - name: <Crank length in Meters>
      type: float
    - name: <Weight in Kilogramms>
      type: float
    - name: Type of gear ratio Sensor=0, fix=1
      type: unsigned short int
    - name: <Real front chain ring>
      type: unsigned short int
    - name: <Real rear sprocket>
      type: unsigned short int
---

<!-- The YAML block above is machine-readable metadata; the Markdown below is for human-readable documentation. -->

cycle
=====

Configuration of the mounted bike

Query command and replies
-------------------------

cycle? → cycle:`<data>`

Configuration command and replies
---------------------------------

cycle=`<data>` → ok or error:`<message>`

Parameters
----------

`<data>` — Parameters of the mounted bike.

- `<wheel size in Meters>`,
- `<Crank length in Meters>`,
- `<Weight in Kilogramms>`,
- `<Type of gear ratio Sensor=0, fix=1>`,
- `<Real front chain ring>`,
- `<Real rear sprocket>`,

Notes
-----

- Version 3.100
- Parameters must not be changed during a running training programme.
- Redevelopments are to apply the `<cycle1>` command.
