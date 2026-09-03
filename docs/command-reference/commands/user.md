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
      ok: user:data
  configuration:
    syntax: user=data
    replies:
      ok: ok
      error: error:message
  parameters:
  - name: data
    type: sequence
    sequence:
    - name: Firstname
      type: char[16]
    - name: Surname
      type: char[16]
    - name: DateOfBirthDay
      type: unsigned short int
    - name: DateOfBirthMonth
      type: unsigned short int
    - name: DateOfBirthYear
      type: unsigned short int
    - name: BodyWeight
      type: float
    - name: DragArea
      type: float
    - name: DragCoefficient
      type: float
---

<!-- The YAML block above is machine-readable metadata; the Markdown below is for human-readable documentation. -->

user
====

Configuration of athlete (out-of-date, use user1!)

Query command and replies
-------------------------

user? → user:`<data>`

Configuration command and replies
---------------------------------

user=`<data>` → ok or error:`<message>`

Parameters
----------

`<data>` — Parameter of athlete.

- `<Firstname>`,
- `<Surname>`,
- `<DateOfBirthDay>`,
- `<DateOfBirthMonth>`,
- `<DateOfBirthYear>`,
- `<BodyWeight>`,
- `<DragArea>`,
- `<DragCoefficient>`

Notes
-----

- Version 3.100
- Parameters must not be changed during a running training programme.
- Note: Changed in version 4; use `<user1>` instead.
