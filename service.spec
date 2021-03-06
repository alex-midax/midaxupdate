# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['service.py'],
             pathex=['D:\\Projects\\midaxupdate_public'],
             binaries=[],
             datas=[('creds/logger/*.json', 'creds/logger'),
             ('creds/reader/*.json', 'creds/reader')],
             hiddenimports=['win32timezone'],
             hookspath=['D:\\Projects\\midaxupdate_public\\hooks'],
             runtime_hooks=['runtime_hooks/create_temp.py'],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='MidaxUpdate',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir='C:/ProgramData/Midax/Update',
          console=True,
          icon='icon/xlogoblack.ico')