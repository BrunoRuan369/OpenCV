import sys
from cx_Freeze import setup, Executable
import re

# Dependencies are automatically detected, but it might need fine tuning.
# "packages": ["os"] is used as example only
build_exe_options = {"packages": ["os"], "excludes": ["tkinter"]}

# base="Win32GUI" should be used only for Windows GUI app
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="Volume Hands Detection",
    version="0.1",
    description="Programa construido para controle de volume atraves de detcçao da mao",
    options={"build_exe": build_exe_options},
    executables=[Executable("volumehands.py", base=base)],
)