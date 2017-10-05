# -*- mode: python -*-

block_cipher = None


a = Analysis(['Timeoffui.py'],
             pathex=['C:/Program Files (x86)/Windows Kits/10/Redist/ucrt/DLLs/x86', 'C:/Python36/Lib/site-packages/PyQt5/Qt/bin', 'D:\\PyCharm\\TimeoffPS'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='TimeoffPC',
          debug=False,
          strip=False,
          upx=True,
          console=False , icon='Aha-Soft-Large-Calendar-Clock.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='TimeoffPC')
