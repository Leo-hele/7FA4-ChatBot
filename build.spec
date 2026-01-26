# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['7FA4chatbot.py'],  # 你的主文件
    pathex=[],  # 搜索路径
    binaries=[],  # 二进制文件
    datas=[('static/api.jimmy',)],  # 数据文件
    hiddenimports=['your_module'],  # 隐藏导入
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=['message.pyd', 'settings.pyd', 'checkLogin.pyd', 'appearance.pyd'],  # 排除pyd，确保不打包进去
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='7FA4聊天器',  # exe名称
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,  # 使用UPX压缩，需要安装UPX
    console=False,  # GUI程序
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='static/7FA4.png',  # 可以添加图标路径
)