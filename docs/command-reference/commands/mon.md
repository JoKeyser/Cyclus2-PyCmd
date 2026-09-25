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
      ok: mon:<Id-Flags>
  configuration:
    syntax: mon=<Id>,<Min>,<Max>,<State>,<Band>
    replies:
      ok: ok
      error: error:<message>
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

Configuration of monitoring (cf. `check`)

Query command and replies
-------------------------

`mon?` 🡺 `mon:<Id-Flags>`

`mon?<Id>` 🡺 `mon:<Id>,<Min>,<Max>`

Configuration command and replies
---------------------------------

`mon=<Id>,<Min>,<Max>,<State>,<Band>` 🡺 `ok` or `error:<message>`

(in slave mode only)

Parameters
----------

- `<Id-Flags>` — Flags of available monitoring items.
  The output is in hexadecimal format.
  For better distinction, the flag `0x8000` is additionally set.
- `<Id>` — Id of monitoring item.
- `<Min>` — Lower limit of training range.
- `<Max>` — Upper limit of training range.
- `<State>` — Monitoring enabled.
- `<Band>` — With colour band.

A description of the flags and IDs is shown in chapter 2.1.
The unit for the parameters `<Min>` and `<Max>` is also documented there.
If a monitoring is to be deleted, the parameter `<State>` must be set to `0`.
The drawing of the colour strip in the diagram can be initiated by setting `<State>`.
Please note that a colour strip can be drawn only for one parameter.

Notes
-----

- Version 4.0
