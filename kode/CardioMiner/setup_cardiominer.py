from cx_Freeze import setup, Executable
import sys

import os


#path to tcl/tk
os.environ['TCL_LIBRARY'] = r'C:\Users\Anne Marie\Anaconda3\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\Users\Anne Marie\Anaconda3\tcl\tk8.6'


buildOptions = {"includes": ["altgraph", "bleach", "certifi", "chardet", "click", "colorama", \
 "cycler", "decorator", "dill", "Django", "entrypoints", "et_xmlfile", "Faker", "Flask", \
  "future", "h5py","hdf5storage","html5lib", "idna", "image", "ipykernel", "ipython",
  "ipython_genutils", "ipywidgets", "itsdangerous", "jdcal", "jedi", "Jinja2", \
    "jsonschema", "jupyter_client", "jupyter_core", "macholib", "MarkupSafe", "matlab", \
     "matplotlib", "mistune", "mritopng", "nbconvert", "nbformat", "networkx", "notebook", \
    "np", "numexpr", "numpy", "mkl", "numutil", "olefile", "openpyxl", "pandas", \
    "pandocfilters", "parso", "pefile", "pickleshare", "plotly", "prompt_toolkit", \
    "pydicom", "Pygments", "pyparsing", "PyQt5", "pyreadline", "pytz", \
    "pywt", "qtgui", "report", "requests",  \
    "scipy", "Send2Trash", "simplegeneric", "sip", "six", "tables", "terminado", \
    "testpath", "text_unidecode", "tornado", "traitlets", "urllib3", "virtualenv", "wcwidth", \
    "webencodings", "werkzeug", "widgetsnbextension", "xlsxwriter", "xlwt", 'numpy.core._methods', \
    'numpy.lib.format', "atexit", "re"], "include_files": ['images/'], \
    "excludes": ["gi", "opencv_python", "Pillow", "pypng", "python_dateutil", "pywin32", "pywinpty", "pyzmq", "sc_pylibs", "scikit_image"]}
# "+mklnumutil" erstattet med "mkl", "numutil"
# fire siste i inkludes utgjør foreløpig ingen forskjell på feilmeldingene ved kjøring av fryst program
# bindestreker erstattet med understreker
#pywavelets erstattet med pywt

base = 'Win32GUI' if sys.platform=='win32' else None


setup(
    name='CardioMiner',
    version = '1.0',
    description = 'CardioMiner-applikasjon',
    options = {"build_exe": buildOptions},
    executables = [Executable("Start.py", base = base)]
)
