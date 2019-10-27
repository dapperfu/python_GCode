"""Unit testing for laser power on anodized aluminum."""

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
    # TODO: Get end-stops installed.
    # cnc.home()
    # Metric
    cnc.cmd("G21")
    # Set this to 0.
    cnc.cmd("G92X0Y0Z0")
    yield cnc
    cnc.cmd("G90")
    cnc.cmd("G0X0Y0F300")


def test_aluminum_laser_power(cnc):
    for power in [100, 150, 200, 255]:
        for row, feed in enumerate([15, 30, 60, 120, 180, 240, 300]):
            row_y = row*5 # Every 5 mm.
            cnc.cmd("G90")
            cnc.cmd(f"G0X0Y{row_y}")
            cnc.run(prog)
                prog = gcode.Line(power=power, feed=feed, machine=cnc)
                cnc.cmd("G91")
                cnc.run(prog)
