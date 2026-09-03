<!--
SPDX-FileCopyrightText: 2022 RBM elektronik-automation GmbH, Weissenfelser Strasse 73, 04229 Leipzig, Germany
SPDX-License-Identifier: NoAssertionLicense
SPDX-Description: Cyclus2 command reference entry derived from the Cyclus2 protocol specification PDF.
-->

---
command:
  name: user1
  summary: Configuration of athlete (new version)
  query:
    syntax: user1?
    replies:
      ok: user1:data
  configuration:
    syntax: user1=data
    replies:
      ok: ok
      error: error:message
  parameters:
  - name: <data>
    type: sequence
    sequence:
    - name: <Version>
      type: unsigned short int
    - name: <Firstname>
      type: char[16]
    - name: <Surname>
      type: char[16]
    - name: <DateOfBirth>
      type: char[11]
    - name: <Gender>
      type: unsigned short int
      values:
      - code: '0'
        meaning: Unknown
      - code: '1'
        meaning: Male
      - code: '2'
        meaning: Female
    - name: <BodyWeight>
      type: float
    - name: <BodyHeight>
      type: float
    - name: <DragArea>
      type: float
    - name: <DragCoefficient>
      type: float
---

<!-- The YAML block above is machine-readable metadata; the Markdown below is for human-readable documentation. -->

user1
=====

Configuration of athlete (new version)

Query command and replies
-------------------------

user1? → user1:`<data>`

Configuration command and replies
---------------------------------

user1=`<data>` → ok or error:`<message>`

Parameters
----------

`<data>` — Parameter of athlete.

- `<Version>`,
- `<Firstname>`,
- `<Surname>`,
- `<DateOfBirth>`,
- `<Gender>`,
- `<BodyWeight>`,
- `<BodyHeight>`,
- `<DragArea>`,
- `<DragCoefficient>`

`<Gender>` — Athlete gender.

- 0 — Unknown.
- 1 — Male.
- 2 — Female.

Notes
-----

- Version 4.2.4155, new version for user.
