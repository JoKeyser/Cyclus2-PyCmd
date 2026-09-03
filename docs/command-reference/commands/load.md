<!--
SPDX-FileCopyrightText: 2022 RBM elektronik-automation GmbH, Weissenfelser Strasse 73, 04229 Leipzig, Germany
SPDX-License-Identifier: NoAssertionLicense
SPDX-Description: Cyclus2 command reference entry derived from the Cyclus2 protocol specification PDF.
-->

---
command:
  name: load
  summary: Configuration of the current load setting
  query:
    syntax: load?
    replies:
      ok: load:<CtrlId>,Val
  configuration:
    syntax: load=CtrlId,Val
    replies:
      ok: ok
      error: error:message
  parameters:
  - name: <CtrlId>
    type: unsigned short int
    values:
    - code: '0'
      meaning: Current load value
    - code: '1'
      meaning: Manual override
    - code: '2'
      meaning: Target load
  - name: <Val>
    type: float
---

<!-- The YAML block above is machine-readable metadata; the Markdown below is for human-readable documentation. -->

load
====

Configuration of the current load setting

Query command and replies
-------------------------

load? → load:`<CtrlId>`,`<Val>`

Configuration command and replies
---------------------------------

load=`<CtrlId>`,`<Val>` → ok or error:`<message>`

Parameters
----------

`<CtrlId>` — Identifier of the controlled load value.

- 0 — Current load value.
- 1 — Manual override.
- 2 — Target load.

`<Val>` — Load value to be set or read.

Notes
-----

- This command is used to read or adjust the active load in the current ergometry mode.
- The exact units are device-dependent and should be interpreted according to the connected equipment.
