<!--
SPDX-FileCopyrightText: 2022 RBM elektronik-automation GmbH, Weissenfelser Strasse 73, 04229 Leipzig, Germany
SPDX-License-Identifier: NoAssertionLicense
SPDX-Description: Cyclus2 command reference entry derived from the Cyclus2 protocol specification PDF.
-->

---
command:
  name: text
  summary: Write text to the info bar
  query:
    syntax: text?
    replies:
      ok: text:data
  configuration:
    syntax: text=data
    replies:
      ok: ok
      error: error:message
  parameters:
  - name: <data>
    type: string
---

<!-- The YAML block above is machine-readable metadata; the Markdown below is for human-readable documentation. -->

text
====

Write text to the info bar

Query command and replies
-------------------------

text? → text:`<data>`

Configuration command and replies
---------------------------------

text=`<data>` → ok or error:`<message>`

Parameters
----------

`<data>` — Text with maximal 63 characters.

The text is displayed in slave mode at the upper margin of the display. The default is „Cyclus2 Interface“.

If the Cyclus2 is switched to slave mode with the parameter 2, no info line will be available (see above).

Notes
-----

- Version 3.100
- Supported in release 5.0
