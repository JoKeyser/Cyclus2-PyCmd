<!--
SPDX-FileCopyrightText: 2022 RBM elektronik-automation GmbH, Weissenfelser Strasse 73, 04229 Leipzig, Germany
SPDX-License-Identifier: NoAssertionLicense
SPDX-Description: Cyclus2 command reference entry derived from the Cyclus2 protocol specification PDF.
-->

---
command:
  name: ergo
  summary: Configuration of ergoline mode
  query:
    syntax: ergo?
    replies:
      ok: ergo:val
  configuration:
    syntax: ergo=val
    replies:
      ok: ok
      error: error:message
  parameters:
  - name: val
    type: unsigned short int
    values:
    - code: '0'
      meaning: Standard; Cyclus2 set back to manual control
    - code: '1'
      meaning: Ergoline mode; Cyclus2 can be controlled with Ergoline commands
    - code: '2'
      meaning: As in 1, but slave mode is automatically quit when ending ergometry
        and displaying analysis results
    - code: '3'
      meaning: Slave mode, operator can use the electronic gear shift, info line not
        displayed
    - code: '4'
      meaning: As in 3, but slave mode is automatically quit when ending ergometry
        and displaying analysis results
    - code: '5'
      meaning: As in 3, but with sending of KeyDown events
    - code: '6'
      meaning: As in 4, but with sending of KeyDown events
---

<!-- The YAML block above is machine-readable metadata; the Markdown below is for human-readable documentation. -->

ergo
====

Configuration of ergoline mode

Query command and replies
-------------------------

ergo? → ergo:`<val>`

Configuration command and replies
---------------------------------

ergo=`<val>` → ok or error:`<message>`

Parameters
----------

`<val>` — Mode.

- 0 — Standard; Cyclus2 is set back to manual control.
- 1 — Ergoline mode; Cyclus2 can be controlled with Ergoline commands.
- 2 — As in 1, but slave mode is automatically quit when ending ergometry and displaying analysis results.
- 3 — Slave mode; operator can use the electronic gear shift, info line is not displayed.
- 4 — As in 3, but slave mode is automatically quit when ending ergometry and displaying analysis results.
- 5 — As in 3, but with sending of KeyDown events.
- 6 — As in 4, but with sending of KeyDown events.

Notes
-----

- As from version 4.0.2895.23909
- Note: Changed in version 4.2.4409.21078
- Supported in release 5.0
