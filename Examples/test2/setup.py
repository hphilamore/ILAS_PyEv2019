import cx_Freeze
import sys

executables = [cx_Freeze.Executable("03_game_template.py")]

cx_Freeze.setup(
    name="A bit Racey",
    options={"build_exe": {"packages":["pygame", "sys", "random", "math"]}},
    executables = executables

    )