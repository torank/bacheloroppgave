from cx_Freeze import setup, Executable
import sys
import os

#path to tcl/tk, needs to be set to the path to the libraries on the speicific computer being used
os.environ['TCL_LIBRARY'] = r'C:\Python36\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\Python36\tcl\tk8.6'

buildOptions = {"includes": ["scipy", "numpy", "matplotlib", "sip", "pyqt5", "numpy.core._methods", "numpy.lib.format", "scipy.sparse.csgraph._validation", "scipy.ndimage._ni_support", "scipy.ndimage._ni_docstrings"], "excludes": ["scipy.spatial.cKDTree"], "include_files": ['EKGmat/']}


base = 'Win32GUI' if sys.platform=='win32' else None


setup(
    name='NEEDED',
    version = '1.0',
    description = 'Needed Applikasjon',
    options = {"build_exe": buildOptions},
    executables = [Executable("new_gui.py", base = base)]
)