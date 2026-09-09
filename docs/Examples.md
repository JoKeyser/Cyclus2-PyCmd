<!--
SPDX-FileCopyrightText: 2022 RBM elektronik-automation GmbH, Weissenfelser Strasse 73, 04229 Leipzig, Germany
SPDX-License-Identifier: NoAssertionLicense
SPDX-Description: Examples from the Cyclus2 protocol specification PDF, converted to Markdown.
SPDX-FileContributor: Johannes Keyser <johannes.keyser@uni-hamburg.de>
-->

# Examples

This file contains examples from chapter 3 of the [Cyclus2 protocol specification PDF](./command-reference/Cyclus2-protocol-specs.pdf).
The PDF's tabular format is reformatted into lists that allow text wrapping for reading on small screens (and perhaps in terminal applications).

If in doubt, please refer to the original PDF for the official content.
If you find errors or discrepancies with the PDF, or you made an interesting example, [please report/contribute them](/README.md#contributing).

Here is how to interpret each step:

- `Command to Cyclus2` 🡺 `Reply from Cyclus2` — Comments/explanations about the command and reply.

Note that steps including _None_ either require no command or send no reply:

- _None_ 🡺 `reply` means that no (additional) command is expected.
- `command` 🡺 _None_ means that the Cyclus2 sends no reply.

## List of examples

- [Example 3.1](#31-preparation-and-settings): Preparation and settings
- [Example 3.2](#32-programme-generation-and-ergometry-control): Programme generation and ergometry control
- [Example 3.3](#33-programme-initialisation-with-stages-and-ergometry-control): Programme initialisation with stages and ergometry control
- [Example 3.4](#34-ergometry-control-from-an-external-system-example-track-pattern): Ergometry control from an external system (example track pattern)
- [Example 3.5](#35-ergometry-control-from-an-external-system-with-ergoline-commands): Ergometry control from an external system with Ergoline commands
- [Example 3.6](#36-control-of-track-simulation): Control of track simulation

## 3.1 Preparation and settings

1. `vers?` 🡺 `vers:Cyclus2,Version 3.100` — Check connectivity and query the software version.
2. `sn?` 🡺 `sn:0297-10020-00100` — Query the serial number.
3. `slave=1` 🡺 `ok` — Switch the Cyclus2 to slave mode.
4. `cycle=2.115,0.172,8.5,1,53,12` 🡺 `ok` — Set the bike parameters: wheel perimeter 2.115 m, crank length 172 mm, weight 8.5 kg, fixed ratio 53/12.
5. `user=Jens,Meyer,10,10,75,72.5,0.44,0.715` 🡺 `ok` — Set athlete data: Jens Meyer, born 10/10/1975, weight 72.5 kg, frontal area 0.44 m², fan friction factor 0.715.
6. `cond=1.202,1` 🡺 `ok` — Preset conditions: cycling on asphalt with air density 1.202 kg/m³.
7. `check?` 🡺 `check:8000` — No monitoring is set.
8. `check=0,70,80` 🡺 `ok` — Set monitoring of cadence. The athlete is to exercise within the range of 70 to 80 1/min.
9. `check?` 🡺 `check:8001` — Cadence flag is set.
10. `check=0,0,0` 🡺 `ok` — Delete monitoring of cadence.
11. `check?` 🡺 `check:8000` — Monitoring is cleared.
12. `graph=1,0,20,1,0,250,5,0,300,1` 🡺 `ok` — Set diagram configuration: 20-minute x-axis, heart rate 0–250 1/min on the left y-axis, performance 0–300 W on the right y-axis, auxiliary grid enabled.

## 3.2 Programme generation and ergometry control

1. `slave?` 🡺 `slave:0` — Cyclus2 is in standard mode.
2. `slave=1` 🡺 `ok` — Switch Cyclus2 to slave mode.
3. `gen=8,3000,0,0,0,100,120,20,1,5,0,10` 🡺 `ok` — Sinus programme with 10 hills with a load continuation of 30 seconds each. The first hill has an amplitude of 120 W, for each of the following hills the amplitude will be increased by 20 W. The load in the valley is 100 W.
4. `data=10` 🡺 `ok` — Setting of a continuous data output once new training data have been retrieved.

   _None_ 🡺 `data:10,<data>` — Data are continuously being sent without prompt. In this case approx. 2 sets of data per second are sent via the serial port. If the data are to be sent via the LAN, the command `data=6` must be used.
5. `ctrl=1` 🡺 `ok` — Start of ergometry.
6. `ctrl=0` 🡺 `ok` — Cancellation of ergometry.
7. `data=0` 🡺 `ok` — Stop continuous data output.
8. `slave=0` 🡺 `ok` — Set Cyclus2 back to standard mode. Cyclus2 can be operated manually.

## 3.3 Programme initialisation with stages and ergometry control

1. `slave?` 🡺 `slave:0` — Cyclus2 is in standard mode.
2. `slave=1` 🡺 `ok` — Switch Cyclus2 to slave mode.
3. `stage?` 🡺 `Stage:30000` — No programme loaded on the Cyclus2.
4. `stage=0,30,200,0,0,5,0` 🡺 `ok` — Initialise first stage of the programme (30 seconds, constant 200 Watt).
5. `stage=1,20,200,150,1,5,0` 🡺 `ok` — Initialise second stage of the programme (the load is decreased from 200 to 150 Watt within 20 seconds).
6. `stage=1,20,150,0,0,5,0` 🡺 `ok` — Initialise third stage of the programme (20 seconds, constant 150 Watt).
7. `stage=1,20,100,0,0,5,0` 🡺 `ok` — Initialise fourth stage of the programme (20 seconds, constant 100 Watt).
8. `stage=1,30,100,200,2,5,0` 🡺 `ok` — Initialise fifth stage of the programme (30 seconds, Sinus from 100 up to 200 Watt).
9. `stage=1,10,200,100,2,5,0` 🡺 `ok` — Initialise sixth stage of the programme (10 seconds, Sinus from 200 down to 100 Watt).
10. `stage=2,20,100,300,3,5,0` 🡺 `ok` — Initialise sixth stage of the programme (20 seconds, Sinus wave with valley 100 and amplitude 300 Watt), and programme preview update.
11. `stage?` 🡺 `Stage:30007` — Programme with seven stages loaded.
12. `data=10` 🡺 `ok` — Setting of a continuous data output once new training data have been retrieved.

    _None_ 🡺 `data:10,<data>` — Data are continuously being sent without prompt. In this case approx. 2 sets of data per second are sent via the serial port. If the data are to be sent via the LAN, the command `data=6` must be used.

13. `ctrl=1` 🡺 `ok` — Start of ergometry.
14. `save=3` 🡺 `ok` — Save ergometry data on USB memory stick or if not present on the network drive.
15. `ctrl=0` 🡺 `ok` — Cancellation of ergometry.
16. `data=0` 🡺 `ok` — Stop continuous data output.

## 3.4 Ergometry control from an external system (example track pattern)

1. `slave?` 🡺 `slave:0` — Cyclus2 is in standard mode.
2. `slave=1` 🡺 `ok` — Switch Cyclus2 to slave mode.
3. `ctrl?` 🡺 `ctrl:0` — There is no ergometry running.
4. `load=6,0` 🡺 `ok` — Preparation of track pattern (Load parameter inclination, initial load 0 %), previously set up ergometry programmes will be deleted.
5. `data=10` 🡺 `ok` — Setting of a continuous data output once new training data have been retrieved.

   _None_ 🡺 `data:10,<data>` — Data are continuously being sent without prompt. In this case approx. 2 sets of data per second are sent via the serial port. If the data are to be sent via the LAN, the command `data=6` must be used.

6. `ctrl=1` 🡺 `ok` — Start of ergometry.

   ... <!-- The ellipsis "..." probably indicates that time may pass here. -->

7. `load=6,0.75` 🡺 `ok` — Set new inclination (0.75 % uphill).

   ... <!-- The ellipsis "..." probably indicates that time may pass here. -->

8. `load=6,-1.25` 🡺 `ok` — Set new inclination (-1.25 % downhill).

   ... <!-- The ellipsis "..." probably indicates that time may pass here. -->

9. `save=3` 🡺 `ok` — Save ergometry data on USB memory stick or if not present on the network drive.
10. `ctrl=0` 🡺 `ok` — Cancellation of ergometry.
11. `data=0` 🡺 `ok` — Stop continuous data output.
12. `slave=0` 🡺 `ok` — Set Cyclus2 clear for operation.

## 3.5 Ergometry control from an external system with Ergoline commands

1. `vers?` 🡺 `vers: Cyclus2, Version 4.0.2895.23809` — Connectivity check and version query.
2. `ergo=1` 🡺 `ok` — Switch Cyclus2 to Ergoline mode. Any ergometry already running will be cancelled. If the Cyclus2 is in analysis mode, it will be switched to standard operation mode.
3. `text=Cyclus2 im Ergoline-Modus` 🡺 `ok` — Text content on the display of the Cyclus2.
4. `graph=1,0,20,1,0,250,5,0,300,1` 🡺 `ok` — Diagram settings (x-axis 20 minutes, left y-axis heart rate from 0-250 1/min, right y-axis performance from 0-300 W, with auxiliary grid).
5. `a90` 🡺 _None_ — Set initial load 90W.
6. `s` 🡺 _None_ — Start ergometry.
7. `b` 🡺 `B090` — Enquire actual power (result 90 W).
8. `h` 🡺 `H102` — Enquire actual heart rate (result 102 1/min).
9. `d` 🡺 `n081` — Enquire actual cadence (result 81 1/min).
10. `w120` 🡺 _None_ — New load preset 120 W.

    ... <!-- The ellipsis "..." probably indicates that time may pass here. -->

11. `save=3` 🡺 `ok` — Save ergometry data on USB memory stick or if not present on the network drive.
12. `f` 🡺 _None_ — Cancellation of ergometry.
13. `ergo=0` 🡺 _None_ — Set Cyclus2 clear for operation.

## 3.6 Control of track simulation

1. `vers?` 🡺 `vers: Cyclus2, Version 4.2.4155.23809` — Connectivity check and version query. Note, some of the commands listed below are available only as from version 4.2.4155.23809!
2. `sn?` 🡺 `sn:0297-10020-00100` — Query of the serial number of the Cyclus2.
3. `slave?` 🡺 `slave:0` — Cyclus2 is in standard mode (no slave mode).
4. `ctrl?` 🡺 `ctrl:0` — There is no ergometry running.
5. `slave=3` 🡺 `ok` — Switches the Cyclus2 to slave mode. Only the virtual gear shift can be operated on the Cyclus2.
6. `user1=0,Max,Superman,11.11.1980,1,78.3,1.805,0.44,0.715` 🡺 `ok` — Initialisation of the athlete. Note: important as body weight and cwA are factors in the calculation of the load reference preset.
7. `cond=1.202,1` 🡺 `ok` — Terms that co-determine the load reference preset.
8. `cycle1=0,2.113,0.1725,8,53,12,53,17` 🡺 `ok` — Initialisation of the bike. Note: important as the parameters of the bike are factors in the calculation of the load reference preset.
9. `cassette=12,13,14,15,16,17,19,21,23,25` 🡺 `ok` — Setting up of the crown gear of cassette at rear wheel hub for virtual gear shifting. Send the command after `cycle1` everytime!
10. `rings=39,53` 🡺 `ok` — Setting up of front chain rings on crank for virtual gear shifting. Send the command after `cycle1` every time!
11. `graph=3,0,25,1,0,250,5,0,500,1` 🡺 `ok` — Diagram settings (x-axis 25 kilometers, left y-axis heart rate from 0-250 1/min, right y-axis power from 0-500 W, with auxiliary grid).
12. `stage=0,0.2,152,154,4,6,3` 🡺 `ok` — Define 1. stage (existing programme will be deleted): 0.2 km from height 152 m to height 154 m.
13. `stage=1,0.3,154,155,4,6,3` 🡺 `ok` — Add 2. stage: 0.3 km from height 154 m to height 155 m.
14. `stage=1,0.5,155,155,4,6,3` 🡺 `ok` — Add 3. stage: 0.5 km from height 155 m to height 155 m.
15. `stage=1,1.2,155,149,4,6,3` 🡺 `ok` — Add 4. stage: 1.2 km from height 155 m to height 149 m.
16. `stage=2,0.5,149,152,4,6,3` 🡺 `ok` — Add final stage and draw load preview: 0.5 km from height 149 m to height 152 m.
17. `data=7` 🡺 `ok` — Data are being sent continuously every 500 ms in format 3 via the Winsocket interface.

    _None_ 🡺 `data:7,0,0,0,0,0,67,0,6.59,0,0,0,0,53,17` — Athlete is not cycling and has a heart rate of 67 1/min.

    _None_ 🡺 `data:7,0,0,0,0,......` — A new set of data every 500 ms.

    ... <!-- The ellipsis "..." probably indicates that time may pass here. -->

18. `ctrl=1` 🡺 `ok` — Start ergometry.
19. `data:7,50,......` 🡺 _None_ — 1. data set during the ergometry.
20. `data:7,102,......` 🡺 _None_ — 2. data set during the ergometry.
21. `ctrl=0` 🡺 `ok` — Cancel track simulation.
22. `data=5` 🡺 _None_ — Stop continuous data output.
23. `slave=0` 🡺 `ok` — Set Cyclus2 clear for operation.
