<!--
SPDX-FileCopyrightText: 2022 RBM elektronik-automation GmbH, Weissenfelser Strasse 73, 04229 Leipzig, Germany
SPDX-License-Identifier: NoAssertionLicense
SPDX-Description: Cyclus2 command reference entry derived from the Cyclus2 protocol specification PDF.
-->

---
command:
  name: data
  summary: Query of exercise data
  query:
    syntax: data?
    replies:
      ok: data:<val>, data
  configuration:
    syntax: data=val
    replies:
      ok: ok
      error: error:message
  parameters:
  - name: <val>
    type: unsigned short int
    values:
    - code: '0'
      meaning: Com Format 1 after query command
    - code: '1'
      meaning: Com Format 2 after query command
    - code: '10'
      meaning: Com Format 1 continued
    - code: '11'
      meaning: Com Format 1 continued.
    - code: '4'
      meaning: Winsock Format 1 after query command.
    - code: '6'
      meaning: Winsock Format 1 continued
    - code: '12'
      meaning: Winsock +Com Format 1 after query command.
    - code: '14'
      meaning: Winsock +Com Format 1 continued
    - code: '2'
      meaning: Com Format 3 after query command.
    - code: '3'
      meaning: Com Format 3 continued
    - code: '5'
      meaning: Winsock Format 3 after query command.
    - code: '7'
      meaning: Winsock Format 3 continued
    - code: '13'
      meaning: Winsock +Com Format 3 after query command.
    - code: '15'
      meaning: Winsock +Com Format 3 continued
  - name: <data>
    type: format-dependent payload
    formats:
    - id: Format 1
      fields:
      - name: Time counted from ergometry start in Milliseconds/10
        type: unsigned int
      - name: <Distance counted from ergometry start in Meters>
        type: float
      - name: <Crank rotations counted from ergometry start>
        type: float
      - name: <Work counted from ergometry start in Joules>
        type: float
      - name: <Cadence in rpm>
        type: float
      - name: <Heart Rate bpm>
        type: float
      - name: Speed in kms/h
        type: float
      - name: <Transmission in Meters>
        type: float
      - name: <Pedal Force in Newtons>
        type: float
      - name: <Power in Watts>
        type: float
      - name: Inclination in %
        type: float
      - name: <Work in Heart Rate Beat in Joules>
        type: float
    - id: Format 2
      fields:
      - name: Time stamp in Milliseconds/10
        type: unsigned int
      - name: Torque in Newton/1000
        type: unsigned short int
      - name: Periodic time of cadence (Bit 0..15)
        type: unsigned short int
      - name: Periodic time of belt pully(Bit 0..15)
        type: unsigned short int
      - name: Periodic time of cadence (Bit 16..23)
        type: unsigned short int
      - name: Periodic time of belt pully (Bit 16..23)
        type: unsigned short int
      - name: <Heart rate in bpm>
        type: unsigned short int
      - name: Gear ratio in 1/1000
        type: unsigned short int
      - name: <Load value>
        type: unsigned short int
      - name: <manual break>
        type: unsigned short int
      - name: <Stage id>
        type: unsigned short int
      - name: <Target value>
        type: float
    - id: Format 3
      fields:
      - name: Time counted from ergometry start in Milliseconds/10
        type: unsigned int
      - name: <Distance counted from ergometry start in Meters>
        type: float
      - name: <Crank rotations counted from ergometry start>
        type: float
      - name: <Work counted from ergometry start in Joules>
        type: float
      - name: <Cadence in rpm>
        type: float
      - name: <Heart Rate bpm>
        type: float
      - name: Speed in kms/h
        type: float
      - name: <Transmission in Meters>
        type: float
      - name: <Pedal Force in Newtons>
        type: float
      - name: <Power in Watts>
        type: float
      - name: Inclination in %
        type: float
      - name: <Work in Heart Rate Beat in Joules>
        type: float
      - name: <virtual chain ring>
        type: unsigned int
      - name: <virtual rear sprocket>
        type: unsigned int
---

<!-- The YAML block above is machine-readable metadata; the Markdown below is for human-readable documentation. -->

data
====

Query of exercise data

Query command and replies
-------------------------

data? → data:`<val>`, `<data>`

Configuration command and replies
---------------------------------

data=`<val>` → ok or error:`<message>`

Parameters
----------

`<val>` — Data format and data flow.

`<data>` — The requested data payload as described by the selected format.

Format 1
--------

- `<Time counted from ergometry start in Milliseconds/10>`,
- `<Distance counted from ergometry start in Meters>`,
- `<Crank rotations counted from ergometry start>`,
- `<Work counted from ergometry start in Joules>`,
- `<Cadence in rpm>`,
- `<Heart Rate bpm>`,
- `<Speed in kms/h>`,
- `<Transmission in Meters>`,
- `<Pedal Force in Newtons>`,
- `<Power in Watts>`,
- `<Inclination in %>`,
- `<Work in Heart Rate Beat in Joules>`

Format 2
--------

- `<Time stamp in Milliseconds/10>`,
- `<Torque in Newton/1000>`,
- `<Periodic time of cadence (Bit 0..15)>`,
- `<Periodic time of belt pully(Bit 0..15)>`,
- `<Periodic time of cadence (Bit 16..23)>`,
- `<Periodic time of belt pully (Bit 16..23)>`,
- `<Heart rate in bpm>`,
- `<Gear ratio in 1/1000>`,
- `<Load value>`,
- `<manual break>`,
- `<Stage id>`,
- `<Target value>`

Format 3
--------

- `<Time counted from ergometry start in Milliseconds/10>`,
- `<Distance counted from ergometry start in Meters>`,
- `<Crank rotations counted from ergometry start>`,
- `<Work counted from ergometry start in Joules>`,
- `<Cadence in rpm>`,
- `<Heart Rate bpm>`,
- `<Speed in kms/h>`,
- `<Transmission in Meters>`,
- `<Pedal Force in Newtons>`,
- `<Power in Watts>`,
- `<Inclination in %>`,
- `<Work in Heart Rate Beat in Joules>`,
- `<virtual chain ring>`,
- `<virtual rear sprocket>`

Notes
-----

- Version 3.100
- Note: Changed in version 4
- Note: Changed in version 4.2.4155
- Suported in release 5
- As from version 4 the format 2 is not supported anymore! Additionally the format 3 with the data for the virtual gear shift is introduced as from version 4.2.4155.
