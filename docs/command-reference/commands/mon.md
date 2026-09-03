<!--
SPDX-FileCopyrightText: 2022 RBM elektronik-automation GmbH, Weissenfelser Strasse 73, 04229 Leipzig, Germany
SPDX-License-Identifier: NoAssertionLicense
SPDX-Description: Cyclus2 command reference entry derived from the Cyclus2 protocol specification PDF.
-->

---
command:
  name: mon
  summary: Configuration of monitoring (cf. check)
  query:
    syntax: mon?
    replies:
      ok: mon:Id-Flags
  configuration:
    syntax: mon=Id, Min, Max,<State>,Band
    replies:
      ok: ok
      error: error:message
  parameters:
  - name: Id-Flags
    type: unsigned short int
  - name: Id
    type: unsigned short int
  - name: Min
    type: float
  - name: Max
    type: float
  - name: State
    type: int
  - name: Band
    type: int
---

<!-- The YAML block above is machine-readable metadata; the Markdown below is for human-readable documentation. -->

mon
===

Configuration of monitoring (cf. check)

Query command and replies
-------------------------

mon? → mon:`<Id-Flags>`

mon? `<Id>` → mon:`<Id>`, `<Min>`, `<Max>`

Configuration command and replies
---------------------------------

mon=`<Id>`, `<Min>`, `<Max>`,`<State>`,`<Band>` → ok or error:`<message>`

Parameters
----------

`<Id-Flags>` — Flags of available monitoring items in hexadecimal format.

`<Id>` — Identifier of the monitoring item.

`<Min>` — Lower limit of the training range.

`<Max>` — Upper limit of the training range.

`<State>` — Monitoring enabled.

`<Band>` — Colour band setting.

Notes
-----

- Version 4.0
- If monitoring is to be deleted, the parameter `<State>` must be set to 0.
- A colour strip can only be drawn for one parameter.
