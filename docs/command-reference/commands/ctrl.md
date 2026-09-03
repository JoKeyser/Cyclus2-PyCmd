<!--
SPDX-FileCopyrightText: 2022 RBM elektronik-automation GmbH, Weissenfelser Strasse 73, 04229 Leipzig, Germany
SPDX-License-Identifier: NoAssertionLicense
SPDX-Description: Cyclus2 command reference entry derived from the Cyclus2 protocol specification PDF.
-->

---
command:
  name: ctrl
  summary: Control of exercise
  query:
    syntax: ctrl?
    replies:
      ok: ctrl:val
  configuration:
    syntax: ctrl=val
    replies:
      ok: ok
      error: error:message
  parameters:
  - name: <val>
    type: unsigned short int
    values:
    - code: '0'
      meaning: Stop exercise or resume after pause, while status is 'no ergometry'
    - code: '1'
      meaning: Start exercise or resume after break, while exercise is running
    - code: '2'
      meaning: Break
---

<!-- The YAML block above is machine-readable metadata; the Markdown below is for human-readable documentation. -->

ctrl
====

Control of exercise

Query command and replies
-------------------------

ctrl? → ctrl:`<val>`

Configuration command and replies
---------------------------------

ctrl=`<val>` → ok or error:`<message>`

Parameters
----------

`<val>` — Status of exercise.

- 0 — Stops exercise or resumes after pause, while status is "no ergometry".
- 1 — Starts exercise or resumes after break, while exercise is running.
- 2 — Break.

Notes
-----

- Version 3.100
- Supported in release 5.0
