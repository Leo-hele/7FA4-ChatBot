# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['7FA4chatbot.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('static/api.jimmy', 'static'),
        ('static/index_to_realname.jimmy', 'static'),
        ('static/realname_to_index.jimmy', 'static'),
        ('static/settings.jimmy', 'static'),
        ('static/7FA4.ico', 'static'),
    ],
    hiddenimports=[
        'Crypto.Cipher',
        'Crypto.Util.Padding'
    ],
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
    name='7FA4chatbot',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=False,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='static/7FA4.ico'
)
