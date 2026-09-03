<!--
SPDX-FileCopyrightText: 2022 RBM elektronik-automation GmbH, Weissenfelser Strasse 73, 04229 Leipzig, Germany
SPDX-License-Identifier: NoAssertionLicense
SPDX-Description: Cyclus2 command reference entry derived from the Cyclus2 protocol specification PDF.
-->

---
command:
  name: save
  summary: Configuration of auto-save after finish of ergometry
  query:
    syntax: save?
    replies:
      ok: save:val
  configuration:
    syntax: save=val
    replies:
      ok: ok
      error: error:message
  parameters:
  - name: val
    type: unsigned short int
    values:
    - code: '0'
      meaning: Ergometry data will not be saved
    - code: '1'
      meaning: Ergometry data will be saved on the USB memory stick
    - code: '2'
      meaning: Ergometry data will be saved on the network drive
    - code: '3'
      meaning: Ergometry data will be saved on the USB memory stick or, if not present,
        on the network drive
---

<!-- The YAML block above is machine-readable metadata; the Markdown below is for human-readable documentation. -->

save
====

Configuration of auto-save after finish of ergometry

Query command and replies
-------------------------

save? → save:`<val>`

Configuration command and replies
---------------------------------

save=`<val>` → ok or error:`<message>`

Parameters
----------

`<val>` — Mode.

- 0 — Ergometry data will not be saved.
- 1 — Ergometry data will be saved on the USB memory stick.
- 2 — Ergometry data will be saved on the network drive.
- 3 — Ergometry data will be saved on the USB memory stick or, if not present, on the network drive.

Notes
-----

- As from version 4.1.3208.22920
