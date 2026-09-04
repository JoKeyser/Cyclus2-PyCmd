<!--
SPDX-FileCopyrightText: 2022 RBM elektronik-automation GmbH, Weissenfelser Strasse 73, 04229 Leipzig, Germany
SPDX-License-Identifier: NoAssertionLicense
SPDX-Description: Cyclus2 command reference index derived from the protocol specification PDF.
SPDX-Contributor: Johannes Keyser <johannes.keyser@uni-hamburg.de>
-->

# Command reference

This directory contains the command reference for the Cyclus2 protocol in three complementary formats.

- The source of truth is the [Cyclus2 protocol specification](./Cyclus2-protocol-specs.pdf), provided as PDF by RBM elektronik-automation GmbH.
  The PDF lists the commands in compact tabular form, which is great for human readers with enough screen space.
- In addition, every command is described in a separate Markdown file with YAML front matter.
  These files allow for easier reading and processing in different contexts like terminals or software tools.
  The goal is to remain true to the PDF content; mismatches are considered bugs and should be reported.
  For more information, see the [file structure of the command reference](#file-structure-of-the-command-reference).

## File structure of the command reference

Each command is in a separate file and follows the same combination of YAML front matter and Markdown body.

- YAML front matter holds the technical protocol data.
  - The command object is keyed under command, so each file can be loaded as a single command entry.
  - The base command name and its query/configuration syntax remain separate.
  - Parameters, replies, enums, and ordered sequences are stored in explicit structures.
  - Format-dependent payloads keep their structure instead of being flattened into a string.
- The Markdown body holds the readable summary and prose from the PDF.
  - It is intended for people, terminal output, and simple rendering (e.g., for the web).
  - Headings are kept short and plain-text friendly.
- The schema is intentionally simple and avoids semantics not present in the PDF.
  - It stays flat for simple commands.
  - It adds nested structures only where the PDF clearly defines a payload or sequence.

## Cyclus2 command set

- [accu](./commands/accu.md) — Query of battery capacity
- [br](./commands/br.md) — Configuration of baud rate
- [calc](./commands/calc.md) — Configuration of calculation parameter
- [cassette](./commands/cassette.md) — Configuration of the cassette with the available rear sprockets for virtual gear shifting
- [check](./commands/check.md) — Configuration of monitoring (cf. mon)
- [cond](./commands/cond.md) — Configuration of external field conditions
- [ctrl](./commands/ctrl.md) — Control of exercise
- [curr](./commands/curr.md) — Query of motor current
- [cycle](./commands/cycle.md) — Configuration of the mounted bike
- [cycle1](./commands/cycle1.md) — Configuration of the mounted bike (new version)
- [data](./commands/data.md) — Query of exercise data
- [eol](./commands/eol.md) — Configuration of the end of line
- [ergo](./commands/ergo.md) — Configuration of ergoline mode
- [gen](./commands/gen.md) — Configuration of ergometry loads with the load generator
- [graph](./commands/graph.md) — Configuration of chart
- [heap](./commands/heap.md) — Query of available heap size
- [jump](./commands/jump.md) — Jump to a load stage
- [keydown](./commands/keydown.md) — KeyDown Events (see above command slave)
- [load](./commands/load.md) — Configuration of the current load setting
- [mct](./commands/mct.md) — Configuration of Maximum Strength Test with hold time
- [mon](./commands/mon.md) — Configuration of monitoring (cf. check)
- [mpt](./commands/mpt.md) — Configuration of Maximum Strength Test
- [obla](./commands/obla.md) — Configuration of the OBLA threshold test
- [os](./commands/os.md) — Query of version of operating system
- [prog](./commands/prog.md) — Query of the current type of ergometry
- [pwc](./commands/pwc.md) — Configuration of the Power Warm-up Cycle
- [rings](./commands/rings.md) — Configuration of the front chain rings for virtual gear shifting
- [save](./commands/save.md) — Configuration of auto-save after finish of ergometry
- [slave](./commands/slave.md) — Configuration of slave mode
- [sn](./commands/sn.md) — Query of serial number
- [stage](./commands/stage.md) — Configuration of load stages
- [temp](./commands/temp.md) — Query of motor temperature
- [text](./commands/text.md) — Write text to the info bar
- [time](./commands/time.md) — Configuration of the local time
- [user](./commands/user.md) — Configuration of athlete (out-of-date, use user1!)
- [user1](./commands/user1.md) — Configuration of athlete (new version)
- [vers](./commands/vers.md) — Query of software version
- [want](./commands/want.md) — Configuration of the threshold of the WAnT test

## Ergoline compatibility subset

The Ergoline-compatible commands are kept in a separate subfolder because they are only meaningful when the Cyclus2 is switched into Ergoline mode via [commands/ergo.md](./commands/ergo.md).

See [ergoline/README.md](./ergoline/README.md) for the compatibility-mode command set.

- [a](./ergoline/a.md) — Initialize the target value of exercise before start
- [b](./ergoline/b.md) — Query of current power
- [d](./ergoline/d.md) — Query of current cadence
- [f](./ergoline/f.md) — Stop exercise
- [h](./ergoline/h.md) — Query of current heart rate
- [i](./ergoline/i.md) — Query of device id
- [l](./ergoline/l.md) — Set load changes in time interval
- [o](./ergoline/o.md) — Query of systole (dummy irrelevant)
- [s](./ergoline/s.md) — Start exercise
- [u](./ergoline/u.md) — Query of diastole (dummy irrelevant)
- [w](./ergoline/w.md) — Set the target value during exercise
- [x](./ergoline/x.md) — Leave slave mode
