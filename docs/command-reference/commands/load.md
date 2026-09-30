<!--
SPDX-FileCopyrightText: 2022 RBM elektronik-automation GmbH, Weissenfelser Strasse 73, 04229 Leipzig, Germany
SPDX-License-Identifier: NoAssertionLicense
SPDX-Description: Cyclus2 command reference entry derived from the Cyclus2 protocol specification PDF.
-->

---
command:
  name: "load"
  summary: "Configuration of the current load setting"
  query:
    syntax: "load?"
    replies:
      ok: "load:<CtrlId>,<Val>"
  configuration:
    syntax: "load=<CtrlId>,<Val>"
    replies:
      ok: "ok"
      error: "error:<message>"
  parameters:
  - name: "CtrlId"
    meaning: "Id of load value"
    type: "unsigned short int"
    values:
    - code: 4
      meaning: "Pedal Force in Newtons"
    - code: 5
      meaning: "Power in Watts"
    - code: 6
      meaning: "Inclination in %"
    - code: 255
      meaning: "will be sent on request"
  - name: "Val"
    type: "float"
---

<!-- The YAML block above is machine-readable metadata; the Markdown below is for human-readable documentation. -->

load
====

Configuration of load value (the same like the manual control mode)

Query command and replies
-------------------------

`load? 🡺 load:<CtrlId>,<Val>`

If no manually controlled ergometry has been set (e.g., during a stage-controlled ergometry), the value `255` is rendered as `<CtrlId>`.
In this case, no further value will be sent for `<Val>`.

Configuration command and replies
---------------------------------

`load=<CtrlId>,<Val>` 🡺 `ok` or `error:<message>`

(in slave mode only)

Parameters
----------

- `<CtrlId>` — Identifier of the controlled load value.
  - `4` — Pedal Force in Newtons
  - `5` — Power in Watts
  - `6` — Inclination in %
  - `255` — will be sent on request (see above)
- `<Val>` — Force value in dependency of `CtrlId` in N, W or %
  - Co-domains:
    - Pedal Force 0..1500 Newtons
    - Power 0..3000 Watts
    - Inclination –25..25 %

Call the load command before starting of ergometry because of initializing of the load type and load value!
So you remove also monitoring settings, start conditions and cancel contitions.
During the ergometry you must not change load type!

An example in chapter 3.4 demonstrates the application of this command.

Notes
-----

- Version 4
- Supported in Release 5.0
