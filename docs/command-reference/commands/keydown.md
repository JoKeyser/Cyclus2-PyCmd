<!--
SPDX-FileCopyrightText: 2022 RBM elektronik-automation GmbH, Weissenfelser Strasse 73, 04229 Leipzig, Germany
SPDX-License-Identifier: NoAssertionLicense
SPDX-Description: Cyclus2 command reference entry derived from the Cyclus2 protocol specification PDF.
-->

---
command:
  name: keydown
  summary: KeyDown Events (see above command slave)
  message: keydown:<keycode>,modifiers
  parameters:
  - name: <keycode>
    type: unsigned short int
  - name: <modifiers>
    type: unsigned short int
---

<!-- The YAML block above is machine-readable metadata; the Markdown below is for human-readable documentation. -->

keydown
=======

KeyDown Events (see above command slave)

Message
-------

keydown:`<keycode>`,`<modifiers>`

Parameters
----------

`<keycode>` — Key Code of the pressed key on the Cyclus2.

`<modifiers>` — Flags of the modifiers like Shift, Control or Alt.

Notes
-----

- Version 4.2.4218
- Supported in release 5.0
- KeyDown events are sent during the slave modes 5 and 6 when the user press a key on the Cyclus2.
