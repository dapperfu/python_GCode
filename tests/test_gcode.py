import uuid

import pytest

import gcode


def test_01(session_uuid, module_uuid, class_uuid, function_uuid):
    print("*" * 50)
    print(f"* Session UUID: {session_uuid}")
    print(f"* Module UUID: {module_uuid}")
    print(f"* Class UUID: {class_uuid}")
    print(f"* Function UUID: {function_uuid}")
    print("*" * 50)


def test_gcode():
    prog = gcode.GCode()
    prog.G0(X=0, Y=0, Z=0)
    print(prog)


def test_G0():
    prog = gcode.GCode()
    prog.G0(X=0, Y=0, Z=0)
    assert "G0" in str(prog)
    assert " " not in str(prog)


def test_add_gcode():
    prog = gcode.GCode()
    prog.G0(X=0, Y=0)
    prog2 = gcode.GCode()
    prog2.G0(X=10, Y=10)
    print(prog + prog2)


def test_add_str():
    prog = gcode.GCode()
    prog.G0(X=0, Y=0)
    prog2 = "G1X10Y10Z0"
    print(prog + prog2)


def test_add_list():
    prog = gcode.GCode()
    prog.G0(X=0, Y=0)
    prog2 = ["G1X10Y10Z0", "G1X20Y20Z0"]
    print(prog + prog2)


@pytest.mark.parametrize("gcode_file", ["circle.ngc"])
def test_load_file(gcode_file):
    prog = gcode.GCode(file="circle.ngc")
    print(prog)


import os


@pytest.mark.parametrize("gcode_file", ["circle.ngc"])
def test_load_save_file(gcode_file):
    base, ext = os.path.splitext(gcode_file)
    out = f"{base}.out.{ext}"

    prog = gcode.GCode(file=gcode_file)
    prog.name = "Test Program"
    prog.save(out)
    prog2 = gcode.GCode(file=out)

    print("Original")
    print(prog)
    print("Reloaded")
    print(prog2)
