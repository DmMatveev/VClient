# -*- mode: python -*-

block_cipher = None


a = Analysis(['vclient\\main.py'],
             pathex=[
             'C:\\Users\\Dmitry\\Desktop\\VClient',
             'C:\\Users\\Dmitry\\Desktop\\VClient\\vclient',
             'C:\\Users\\Dmitry\\Desktop\\VClient\\venv\\Lib\site-packages'
             ],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
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
          name='VBot',
          debug=True,
          bootloader_ignore_signals=False,
          strip=False,
          upx=False,
          runtime_tmpdir=None,
          console=True , icon='icon.ico')
