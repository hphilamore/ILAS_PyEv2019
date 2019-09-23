import cx_Freeze
import sys

executables = [cx_Freeze.Executable("05_space_game.py")]

cx_Freeze.setup(
    name="A bit Racey",
    options={"build_exe": {"packages":["pygame", "sys", "random", "math"]}},
    executables = executables

    )