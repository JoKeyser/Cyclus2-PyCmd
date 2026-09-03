<!--
SPDX-FileCopyrightText: 2022 RBM elektronik-automation GmbH, Weissenfelser Strasse 73, 04229 Leipzig, Germany
SPDX-License-Identifier: NoAssertionLicense
SPDX-Description: Cyclus2 command reference entry derived from the Cyclus2 protocol specification PDF.
-->

---
command:
  name: prog
  summary: Query of the current type of ergometry
  query:
    syntax: prog?
    replies:
      ok: prog:val
  parameters:
  - name: <val>
    type: unsigned short int
    values:
    - code: '0'
      meaning: No programme
    - code: '1'
      meaning: User-defined programme
    - code: '2'
      meaning: Preset test or workout
    - code: '3'
      meaning: Custom ergometry mode
    - code: '4'
      meaning: Maintenance or calibration mode
---

<!-- The YAML block above is machine-readable metadata; the Markdown below is for human-readable documentation. -->

prog
====

Query of the current type of ergometry

Query command and replies
-------------------------

prog? → prog:`<val>`

Parameters
----------

`<val>` — Current ergometry program type.

- 0 — No programme.
- 1 — User-defined programme.
- 2 — Preset test or workout.
- 3 — Custom ergometry mode.
- 4 — Maintenance or calibration mode.

Notes
-----

- See the related command family for the active protocol and training programme state.
- The exact interpretation of the value depends on the connected device and firmware.
