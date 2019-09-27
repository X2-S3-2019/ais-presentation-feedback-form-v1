# -*- mode: python -*-

block_cipher = None


a = Analysis(['web'],
             pathex=['/Users/wangdianwen/Projects/Assignment1'],
             binaries=[],
             datas=[('/usr/local/lib/python2.7/site-packages/eel/eel.js', 'eel'), ('accessment.py', 'accessment.py')],
             hiddenimports=['bottle_websocket'],
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
          a.binaries,
          a.zipfiles,
          a.datas,
          name='web',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True )
