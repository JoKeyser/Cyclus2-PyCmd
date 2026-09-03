<!--
SPDX-FileCopyrightText: 2022 RBM elektronik-automation GmbH, Weissenfelser Strasse 73, 04229 Leipzig, Germany
SPDX-License-Identifier: NoAssertionLicense
SPDX-Description: Cyclus2 command reference entry derived from the Cyclus2 protocol specification PDF.
-->

---
command:
  name: time
  summary: Configuration of the local time
  query:
    syntax: time?
    replies:
      ok: time:data
  configuration:
    syntax: time=data
    replies:
      ok: ok
      error: error:message
  parameters:
  - name: <data>
    type: date/time string
---

<!-- The YAML block above is machine-readable metadata; the Markdown below is for human-readable documentation. -->

time
====

Configuration of the local time

Query command and replies
-------------------------

time? → time:`<data>`

Configuration command and replies
---------------------------------

time=`<data>` → ok or error:`<message>`

Parameters
----------

`<data>` — local time with format `dd.mm.yyyy hh:nn:ss`.

Notes
-----

- Version 3.100
- Supported in release 5.0
