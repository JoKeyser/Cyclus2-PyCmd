<!--
SPDX-FileCopyrightText: 2022 RBM elektronik-automation GmbH, Weissenfelser Strasse 73, 04229 Leipzig, Germany
SPDX-License-Identifier: NoAssertionLicense
SPDX-Description: Cyclus2 command reference entry derived from the Cyclus2 protocol specification PDF.
-->

---
command:
  name: accu
  summary: Query of battery capacity
  query:
    syntax: accu?
    replies:
      ok: accu:present[,<val>]
  parameters:
  - name: <present>
    type: unsigned short int
  - name: <val>
    type: float
---

<!-- The YAML block above is machine-readable metadata; the Markdown below is for human-readable documentation. -->

accu
====

Query of battery capacity

Query command and replies
-------------------------

accu? → accu:`<present>`[,`<val>`]

Parameters
----------

`<present>` — Battery state.

- 0 — Cyclus2 without battery.
- 1 — Cyclus2 with battery; `<val>` is battery voltage in volts.
- 2 — Cyclus2 with battery; `<val>` is capacity in percent.

`<val>` — Battery voltage or capacity, depending on `<present>`.

Notes
-----

- Version 3.100
- New as from version 4.2.4155: the capacity of the rechargeable battery is rendered in volts or percent, depending on the type of brake aggregate used.
- Supported in release 5.0
