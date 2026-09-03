<!--
SPDX-FileCopyrightText: 2022 RBM elektronik-automation GmbH, Weissenfelser Strasse 73, 04229 Leipzig, Germany
SPDX-License-Identifier: NoAssertionLicense
SPDX-Description: Cyclus2 command reference index derived from the protocol specification PDF.
-->

# Ergoline compatibility commands

This folder contains the legacy Ergoline-compatible subset described in the Cyclus2 protocol specification.

These commands are not part of the native Cyclus2 command set. They only make sense after switching the device into Ergoline mode with the main command [ergo](../commands/ergo.md).

## Why this is separate

The PDF treats this as a compatibility section rather than a normal sibling command family.
That is why it is kept apart from the main reference:

- the commands are only meaningful in Ergoline mode
- they are a compatibility layer for older software and drivers
- they are not the default command namespace for new software

## Entry point

Use [ergo](../commands/ergo.md) to switch to Ergoline-compatible operation before using the commands below.

## Command list

- [a](./a.md) — Initialize the target value of exercise before start
- [b](./b.md) — Query of current power
- [d](./d.md) — Query of current cadence
- [f](./f.md) — Stop exercise
- [h](./h.md) — Query of current heart rate
- [i](./i.md) — Query of device id
- [l](./l.md) — Set load changes in time interval
- [o](./o.md) — Query of systole (dummy irrelevant)
- [s](./s.md) — Start exercise
- [u](./u.md) — Query of diastole (dummy irrelevant)
- [w](./w.md) — Set the target value during exercise
- [x](./x.md) — Leave slave mode
