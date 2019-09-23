import cx_Freeze
import sys

executables = [cx_Freeze.Executable("space_test.py")]

cx_Freeze.setup(
    name="A bit Racey",
    options={"build_exe": {"packages":["pygame", "sys", "random", "math"],
                           "include_files":["../../Sounds/battleThemeB.mp3",
                                            "../../img/space.jpg",
                                            "../../img/saucer.png",
                                            "../../img/fire.png",
                                            "../../img/monster.png",
                                            "../../Sounds/zap8a.ogg"]}},
    executables = executables

    )