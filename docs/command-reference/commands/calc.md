<!--
SPDX-FileCopyrightText: 2022 RBM elektronik-automation GmbH, Weissenfelser Strasse 73, 04229 Leipzig, Germany
SPDX-License-Identifier: NoAssertionLicense
SPDX-Description: Cyclus2 command reference entry derived from the Cyclus2 protocol specification PDF.
-->

---
command:
  name: calc
  summary: Configuration of calculation parameter
  query:
    syntax: calc?
    replies:
      ok: calc:<interval>, avg
  configuration:
    syntax: calc=interval,avg
    replies:
      ok: ok
      error: error:message
  parameters:
  - name: interval
    type: unsigned short int
  - name: avg
    type: unsigned short int
---

<!-- The YAML block above is machine-readable metadata; the Markdown below is for human-readable documentation. -->

calc
====

Configuration of calculation parameter

Query command and replies
-------------------------

calc? → calc:`<interval>`, `<avg>`

Configuration command and replies
---------------------------------

calc=`<interval>`,`<avg>` → ok or error:`<message>`

Parameters
----------

`<interval>` — Minimum time in ms/10 between two data requests exchanged between control device and brake aggregate.

`<avg>` — Number of data sets used for floating mean value calculation during training data processing.

Notes
-----

- Version 3.100
- Note: as from version 4 no longer existent
