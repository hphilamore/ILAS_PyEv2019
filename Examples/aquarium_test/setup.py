import cx_Freeze
import sys

executables = [cx_Freeze.Executable("aquarium_animated.py")]

cx_Freeze.setup(
    name="A bit Racey",
    options={"build_exe": {"packages":["pygame", "sys", "random", "math"]}},
    executables = executables

    )