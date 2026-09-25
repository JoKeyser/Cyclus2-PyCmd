<!--
SPDX-FileCopyrightText: 2022 RBM elektronik-automation GmbH, Weissenfelser Strasse 73, 04229 Leipzig, Germany
SPDX-License-Identifier: NoAssertionLicense
SPDX-Description: Cyclus2 command reference entry derived from the Cyclus2 protocol specification PDF.
-->

---
command:
  name: user
  summary: Configuration of athlete (out-of-date, use user1!)
  query:
    syntax: user?
    replies:
      ok: user:<data>
  configuration:
    syntax: user=<data>
    replies:
      ok: ok
      error: error:<message>
  parameters:
  - name: data
    type: sequence
    sequence:
    - name: Firstname max. size 15
      type: char[16]
    - name: Surname max. size 15
      type: char[16]
    - name: Date of birth - day (1..31)
      type: unsigned short int
    - name: Date of birth - month (1..12)
      type: unsigned short int
    - name: Date of birth - year (0..99)
      type: unsigned short int
    - name: Body weight in Kilogramms
      type: float
    - name: Drag area in m²
      type: float
    - name: Drag coefficient cw
      type: float
---

<!-- The YAML block above is machine-readable metadata; the Markdown below is for human-readable documentation. -->

user
====

Configuration of athlete (**out-of-date, use `user1`**!)

Query command and replies
-------------------------

`user?` 🡺 `user:<data>`

Configuration command and replies
---------------------------------

`user=<data>` 🡺 `ok` or `error:<message>`

(in slave mode only)

Parameters
----------

`<data>` — Parameter of athlete.

- `<Firstname max. size 15>`,
- `<Surname max. size 15>`,
- `<Date of birth - day (1..31)>`,
- `<Date of birth - month (1..12)>`,
- `<Date of birth - year (0..99)>`,
- `<Body weight in Kilogramms>`,
- `<Drag area in m²>`,
- `<Drag coefficient cw>`

New as from version 4

Apart from the range of values 0..99 for the year of birth, the range from greater than 1900 to inclusive the year set on the Cylus2 are accepted as parameter.
Data for the year are rendered as 4-digit values.

Notes
-----

- Version 3.100
- Parameters must not be changed during a running training programme.
- Note the change in version 4: Redevelopments are to apply the `user1` command.
