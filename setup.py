import cx_Freeze
import sys
import os

if sys.platform=='win32':
    base = 'Win32GUI'

os.environ['TCL_LIBRARY']= r"C:\Users\Md Rezaul Islam\AppData\Local\Programs\Python\Python38-32\tcl\tcl8.6"
os.environ['TK_LIBRARY']=r"C:\Users\Md Rezaul Islam\AppData\Local\Programs\Python\Python38-32\tcl\tk8.6"

executables = [cx_Freeze.Executable('application.py',base=base, icon='icon.ico')]

cx_Freeze.setup(
    name = 'Rezaul Text Editor',
    options = {"build_exe":{"packages":["tkinter","os"],"include_files":["icon.ico","tcl86t.dll","tk86t.dll",'icons_images']}},
    version = '1.0',
    description = "A Python Tkinter Application",
    executables = executables
)