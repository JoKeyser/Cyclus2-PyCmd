<!--
SPDX-FileCopyrightText: 2022 RBM elektronik-automation GmbH, Weissenfelser Strasse 73, 04229 Leipzig, Germany
SPDX-License-Identifier: NoAssertionLicense
SPDX-Description: Cyclus2 command reference entry derived from the Cyclus2 protocol specification PDF.
-->

---
command:
  name: want
  summary: Configuration of Wingate Anaerobic Test
  query:
    syntax: want?
    replies:
      ok: want:<val>[,<data>]
  configuration:
    syntax: want=val,data
    replies:
      ok: ok
      error: error:message
  parameters:
  - name: val
    type: unsigned short int
    values:
    - code: 12
      meaning: Data <data> are available, Wingate Anaerobic Test
    - code: else
      meaning: no parameter of Maximum Cadence Test available
  - name: data
    type: sequence
    sequence:
    - name: Profile
      type: int
    - name: Factor
      type: float
    - name: Time
      type: float
    - name: StartCadence
      type: float
---

<!-- The YAML block above is machine-readable metadata; the Markdown below is for human-readable documentation. -->

want
====

Configuration of Wingate Anaerobic Test

Query command and replies
-------------------------

`want?` 🡺 `want:<val>[, <data>]`

Configuration command and replies
---------------------------------

`want=<val>,<data>` 🡺 `ok` or `error:<message>`

Parameters
----------

- `<val>` — Type of ergometry.
  - `12` — Data `<data>` are available, Wingate Anaerobic Test
  - else — no parameter of Maximum Cadence Test available
- `<data>` — Parameter of Wingate Anaerobic Test
  - `<Profile >`,
  - `<Factor>`,
  - `<Time>`,
  - `<StartCadence>`

A description of the individual parameters is shown in chapter 2.6.
When writing always set for `<val> = 12`.

Notes
-----

- Version 3.100
- Parameters must not be changed during a running training programme.
