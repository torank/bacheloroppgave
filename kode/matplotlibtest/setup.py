from cx_Freeze import setup, Executable
import sys

import os

#path to tcl/tk
os.environ['TCL_LIBRARY'] = r'C:\Python36\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\Python36\tcl\tk8.6'

buildOptions = {"includes": ["tkinter", "matplotlib", "numpy.core._methods", "numpy.lib.format", "tkinter.filedialog", "matplotlib.legend_handler"], "include_files": ["sampleData.txt"]}


base = 'Win32GUI' if sys.platform=='win32' else None

setup(
    name='Testgui',
    version = '0.1',
    description = 'Program for testing av frysing av matplotlib',
    options = {"build_exe": buildOptions},
    executables = [Executable("test.py", base = base)]
)
