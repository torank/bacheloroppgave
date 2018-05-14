# -*- mode: python -*-

block_cipher = None




a = Analysis(['new_gui.py'],
             pathex=['C:\\Users\\torbj\\NEEDED'],
             binaries=[ ('C:\\Program Files (x86)\\Microsoft SDKs\\Windows\\v10.0A\\bin', 'W10SDKdlls'),
			( 'C:\\Program Files (x86)\\Microsoft Visual Studio 14.0\\VC', 'dlls_fra_MCVS' ),
			('C:\\Windows\\WinSxS\\x86_microsoft-windows-m..namespace-downlevel_31bf3856ad364e35_10.0.16299.15_none_0260a8244e79155d', 'notFoundDLLs')],
             datas=[ ('EKGmat', 'EKGmat') ],
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
          name='new_gui',
          debug=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='new_gui')
