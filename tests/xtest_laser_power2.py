import time

import grbl
import pytest

import gcode


@pytest.fixture(scope="session")
def cnc(request):
    grbl_cfg = {
        "port": request.config.getoption("--port"),
        "baudrate": request.config.getoption("--baudrate"),
    }
    cnc = grbl.Grbl(**grbl_cfg)
    time.sleep(2)
    cnc.reset()
    # Metric
    cnc.cmd("G21")
    cnc.cmd("G91")
    cnc.cmd("G0X5Y5F300")
    # Set this to 0.
    # TODO: Get end-stops installed.
    cnc.cmd("G92X0Y0Z0")
    yield cnc
    cnc.cmd("G90")
    cnc.cmd("G0X0Y0F300")


def test_default_line():
    print(gcode.Line())


def test_00_row1(cnc):
    prog = gcode.GCode(machine=cnc)
    prog.G90()
    prog.G0(X=0, Y=0)
    prog.run()
    cnc.reset()


@pytest.mark.parametrize("laser_power", [10, 50, 75, 100, 150, 200, 255])
def test_01_laser_power(cnc, laser_power):
    prog = gcode.Line(power=laser_power, machine=cnc)
    cnc.cmd("G91")
    prog.run()
    cnc.reset()


def test_02_row2(cnc):
    prog = gcode.GCode(machine=cnc)
    prog.G90()
    prog.G0(X=0, Y=10)
    prog.run()
    cnc.reset()


@pytest.mark.parametrize("feed", [30, 60, 120, 180, 240, 300])
def test_03_laser_feed(cnc, feed):
    prog = gcode.Line(power=255, feed=feed, machine=cnc)
    cnc.cmd("G91")
    prog.run()
    cnc.reset()


def test_04_row3(cnc):
    prog = gcode.GCode(machine=cnc)
    prog.G90()
    prog.G0(X=0, Y=20)
    prog.run()
    cnc.reset()


@pytest.mark.parametrize("dynamic_power", [True, False])
@pytest.mark.parametrize("power", [150, 200, 255])
@pytest.mark.parametrize("feed", [30, 180])
def test_05_laser_power_feed(cnc, dynamic_power, power, feed):
    prog = gcode.Line(machine=cnc, dynamic_power=dynamic_power, power=power, feed=feed)
    cnc.cmd("G91")
    prog.run()
    cnc.reset()
