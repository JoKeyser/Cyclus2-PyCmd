<!--
SPDX-FileCopyrightText: 2022 RBM elektronik-automation GmbH, Weissenfelser Strasse 73, 04229 Leipzig, Germany
SPDX-License-Identifier: NoAssertionLicense
SPDX-Description: Cyclus2 command reference entry derived from the Cyclus2 protocol specification PDF.
-->

---
command:
  name: slave
  summary: Configuration of slave mode
  query:
    syntax: slave?
    replies:
      ok: slave:val
  configuration:
    syntax: slave=val
    replies:
      ok: ok
      error: error:message
  parameters:
  - name: <val>
    type: unsigned short int
    values:
    - code: '0'
      meaning: Standard-mode
    - code: '1'
      meaning: Slave-Mode, Cyclus2 can be controlled via the interfaces only.
    - code: '2'
      meaning: as in 1, but slave mode is automatically quit when ending the ergometry
        and displaying the analysis results (new as from version 4.2.4155)
    - code: '3'
      meaning: Slave-Mode, operator can use the electronic gear shift, the info line
        is not displayed (new as from version 4.2.4155)
    - code: '4'
      meaning: as in 3, but slave mode is automatically quit when ending the ergometry
        and displaying the analysis results (new as from version 4.2.4155)
    - code: '5'
      meaning: as in 3, but with sending of KeyDown events (new as from version 4.2.4218)
    - code: '6'
---

<!-- The YAML block above is machine-readable metadata; the Markdown below is for human-readable documentation. -->

slave
=====

Configuration of slave mode

Query command and replies
-------------------------

slave? → slave:`<val>`

Configuration command and replies
---------------------------------

slave=`<val>` → ok or error:`<message>`

Parameters
----------

`<val>` — Mode.

- 0 — Standard-mode
- 1 — Slave-Mode, Cyclus2 can be controlled via the interfaces only.
- 2 — as in 1, but slave mode is automatically quit when ending the ergometry and displaying the analysis results (new as from version 4.2.4155)
- 3 — Slave-Mode, operator can use the electronic gear shift, the info line is not displayed (new as from version 4.2.4155)
- 4 — as in 3, but slave mode is automatically quit when ending the ergometry and displaying the analysis results (new as from version 4.2.4155)
- 5 — as in 3, but with sending of KeyDown events (new as from version 4.2.4218)
- 6 — as in 4, but with sending of KeyDown events (new as from version 4.2.4218)

Notes
-----

- Version 3.100
- Note: Changed in version 4.2.4155 and 4.2.4218
- Supported in version 5
