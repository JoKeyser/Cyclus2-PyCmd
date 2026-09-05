# -*- mode: python ; coding: utf-8 -*-
#
# PURPOSE: PyInstaller config for the standalone executables.
# SUMMARY: The data files are bundled into the executable so the app can load
#          its command reference and current version number at runtime.
#
# SPDX-FileCopyrightText: Johannes Keyser <johannes.keyser@uni-hamburg.de>
# SPDX-License-Identifier: CC0-1.0


a = Analysis(
    ['Cyclus2-PyCmd.py'],
    pathex=[],
    binaries=[],
    datas=[('docs/command-reference', 'docs/command-reference'), ('VERSION', '.')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='Cyclus2-PyCmd',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
