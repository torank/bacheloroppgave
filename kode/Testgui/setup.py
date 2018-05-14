from cx_Freeze import setup, Executable
import sys

import os

#path to tcl/tk
os.environ['TCL_LIBRARY'] = r'C:\Python36\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\Python36\tcl\tk8.6'

buildOptions = {"includes": ["tkinter"], "include_files": []}

base = 'Win32GUI' if sys.platform=='win32' else None

setup(
    name='Testgui',
    version = '0.1',
    description = 'Knappeprogram',
    options = {"build_exe": buildOptions},
    executables = [Executable("testgui.py", base = base)]
)
