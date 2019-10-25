import grbl
import pytest
import time
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
    yield cnc


def test_default_line(side):
    print(gcode.Line())


@pytest.mark.parametrize("laser_power", [1, 5, 10])
def test_laser_power(cnc, laser_power):
    cnc.reset()
    cnc.cmd("$3=3")
    cnc.reset()
    cnc.cmd("G91")
    cnc.cmd("G21")
    cnc.cmd("G92X0Y0Z0")
    prog = gcode.Line(power=laser_power, machine=cnc)
    prog.run()
