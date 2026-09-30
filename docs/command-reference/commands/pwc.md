<!--
SPDX-FileCopyrightText: 2022 RBM elektronik-automation GmbH, Weissenfelser Strasse 73, 04229 Leipzig, Germany
SPDX-License-Identifier: NoAssertionLicense
SPDX-Description: Cyclus2 command reference entry derived from the Cyclus2 protocol specification PDF.
-->

---
command:
  name: "pwc"
  summary: "Configuration of PWC Test (Physical Working Capacity Test)"
  query:
    syntax: "pwc?"
    replies:
      ok: "pwc:<val>[,<data>]"
  configuration:
    syntax: "pwc=<val>,<data>"
    replies:
      ok: "ok"
      error: "error:<message>"
  parameters:
  - name: "val"
    type: "unsigned short int"
    values:
    - code: 13
      meaning: "Data <data> are available, PWC Test"
    - code: else
      meaning: "No parameter of PWC Test available"
  - name: "data"
    type: "sequence"
    sequence:
    - name: "Protocol"
      type: "int"
    - name: "Start"
      type: "float"
    - name: "Step"
      type: "float"
    - name: "Cadence"
      type: "float"
    - name: "LenType"
      type: "int"
    - name: "Len"
      type: "float"
    - name: "CoolDownLenType"
      type: "int"
    - name: "CoolDownLen"
      type: "float"
    - name: "CoolDownPower"
      type: "float"
---

<!-- The YAML block above is machine-readable metadata; the Markdown below is for human-readable documentation. -->

pwc
===

Configuration of PWC Test (Physical Working Capacity Test)

Query command and replies
-------------------------

`pwc?` 🡺 `pwc:<val>[,data]`

Configuration command and replies
---------------------------------

`pwc=<val>,<data>` 🡺 `ok` or `error:<message>`

(in slave mode only)

Parameters
----------

- `<val>` — Type of ergometry.
  - `13` Data `<data>` are available, PWC Test
  - else — No parameter of PWC Test available
- `<data>` — Parameters of PWC Test.
  - `<Protocol>`,
  - `<Start>`,
  - `<Step>`,
  - `<Cadence>`,
  - `<LenType>`,
  - `<Len>`,
  - `<CoolDownLenType>`,
  - `<CoolDownLen>`,
  - `<CoolDownPower>`

A description of the individual parameters is shown in chapter 2.8.
When writing always set for `<val> = 13`.

Notes
-----

- Version 4.0
- Parameters must not be changed during a running training programme.
