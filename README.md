<!--
SPDX-FileCopyrightText: Johannes Keyser <johannes.keyser@uni-hamburg.de>
SPDX-License-Identifier: EUPL-1.2
-->

# Cyclus2-PyCmd

A command-line interface to interactively send commands to [Cyclus2 ergometers](https://www.cyclus2.com/en/).

> [!warning]
> 🚧 This is prototyping in progress. 🚧

![logo](./media/logo-Cyclus2-PyCmd.svg){width=120}

## Description

This project offers a command-line interface to interactively send commands to a [Cyclus2 ergometer](https://www.cyclus2.com/en/) by RBM elektronik-automation GmbH.

Cyclus2 ergometers include a command interface that can be accessed over a serial interface, Ethernet cable, or WiFi.
Via that interface, you can request data and/or send commands in (near) real-time.
This project provides a simple Python-based command-line interface for interactive exploration.
Eventually, this project can serve as a starting point for more sophisticated programming-based interaction with the Cyclus2.

## Usage

Using this script requires some [Installation](#installation) and [Setup](#setup), see sections below.

Then you can run the code:

```sh
python Cyclus2-PyCmd.py
```

### Example session

```txt
$ python Cyclus2-PyCmd.py
Connected to 192.168.1.200:25000, assuming it is a Cyclus2 ergometer.
Type any Cyclus2 command or type `quit` or `exit` to end the session.
For example, try `vers?` and press <Return> for the software version.

> vers?
vers:Cyclus2, Version 5.0.9083.30724

> data?
data:0,0,0.00,0.00,0.00,0.00,0.00,0.00,8.61,0.00,0.00,0.00,0.00

> something-wrong
error:unknown command

> exit
Closing the connection to the Cyclus2 ergometer.
```

> [!NOTE]
> The Cyclus2 will send "`error:unknown command`" either the command you entered is unknown/invalid, or if the [setup](#setup) is not correct (i.e., not yet logged in as Admin, or the command connection was not enabled).

## Installation

0. You need [Python](http://python.org) on your computer:
   To install Python, use a method appropriate to your computer and, if applicable, your institutional tools/policies.
1. Clone or download this project to your computer, e.g.:

   ```sh
   git clone https://gitlab.rrz.uni-hamburg.de/dhprl/software/Cyclus2-PyCmd.git
   ```

On your Cyclus2, all required software should be installed, but it requires some [setup, see next section](#setup).

## Setup

To use this script, you need a working network connection to your Cyclus2 ergometer and enable a command connection on the Cyclus2.

### Network connection

You need to set up a network connection to your Cyclus2 ergometer, e.g. via a direct Ethernet cable.

- Make sure your computer and the Cyclys2 share the same network.
  For example, you can assign the Cyclus2 a fixed IP address like `192.168.1.200` and your computer an address like `192.168.1.100`.
  Alternatively, use a DHCP server to assign addresses automatically.

- Make sure you can ping the ergometer from your computer, e.g., `ping 192.168.1.200`.
  You should see something like `Reply from 192.168.1.200`.

### Enable command connection on the Cyclus2

1. On the Cyclus2, login as _Admin_ by selecting _System → Login_ and entering the administrator password.
   In the bottom right corner, you should see "Admin" now.
2. On the Cyclus2, enable connections by selecting _System → Connect_.
   You should see a dialog like this:

   ![Screenshot Cyclus2: System → Connect dialog.](./media/screenshot-Cyclus2-System-Connect-dialog.png){width=400}

   Once you press the OK button on the Cyclus2 (or click checkmark if you're using VNC), the Cyclus2 will be ready to accept connections.
   The menu bar at the top of the Cyclus2 screen should now only show "Cyclus2 Interface" instead of the menu items:

   ![Screenshot Cyclus2: Interface, ready to connect.](./media/screenshot-Cyclus2-Interface-ready-to-connect.png){width=400}

## Support

This project is provided in the hope to be useful, without warranties of any kind (see also section [License](#license)).
No support is included, but feel free to reach out to the [authors](#authors) to ask for help.

At this point, this script was only tested on Ubuntu 24.04 LTS with Python 3.12.

## Roadmap

- Document how to setup and use it, along with some simple examples.
- Test on Windows and perhaps MacOS.
- Add more explanation what's going on inside the code and during the session (e.g., on what level are errors happening?).
- Discuss with RBM about command documentation inside this project and/or where to get more information.

## Contributing

Any contribution will be very welcome.
At this stage, please write an email to the authors to report issues, discuss feature requests, or offer patches.
As user of [UHH GitLab](https://gitlab.rrz.uni-hamburg.de), you can also use the GitLab functions.

## Authors

- Johannes Keyser <johannes.keyser@uni-hamburg.de>

## License

This project aims to be [REUSE compliant](https://reuse.software/), indicating for each file the license and copyright information.

All software code is licensed under the European Union Public License (EUPL-1.2) to allow free use and modification, while ensuring that any modifications are also shared under the same license.
See English license text in [LICENSES/EUPL-1.2.txt](./LICENSES/EUPL-1.2.txt); for other languages, see <https://interoperable-europe.ec.europa.eu/collection/eupl/eupl-text-eupl-12>.

Other materials (so far) are licensed under CC0 1.0 Universal Public Domain Dedication for maximal reusability.
See English license text in [LICENSES/CC0-1.0.txt](./LICENSES/CC0-1.0.txt); for a summary and other languages, see <https://creativecommons.org/publicdomain/zero/1.0/deed>.

## Project status

Experimental:
This project is currently being prototyped.
Expect breaking changes at any moment.
