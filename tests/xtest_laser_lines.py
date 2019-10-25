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
    cnc.cmd("M5")
    cnc.cmd("G90")
    cnc.cmd("G0X0Y0F300")


def init(**kwargs):
    prog = gcode.GCode(**kwarg)
    prog.G21()
    prog.G90()
    prog.G92(X=0, Y=0)
    prog.G1(F=200)
    prog.G0(F=200)
    return prog


# Default GCode program fixture with
@pytest.fixture(scope="function")
def prog(cnc):
    """
    Basic Machine Init.
    """
    return init(machine=cnc)


def test_line(prog):
    # Line spacing to use.
    line_spacing = 2.5
    # Generate points for a 10mm line
    line_points = gcode.hline(Xf=10)
    # For each of the given powers
    for p, power in enumerate([50, 75, 100, 150, 175, 200, 255]):
        # Use Absolute coordinates
        prog.G90()
        # Go to a the start of a row, each power has its own row.
        prog.G0(X=0, Y=p * line_spacing)
        # Relative coordinates for each drawn line.
        prog.G91()
        # Using and not using dynamic power.
        for d, dynamic_power in enumerate([True, False]):
            # For each of the given feed rates
            for f, feed in enumerate([30, 60, 120, 180, 240, 300]):
                line = gcode.Line(
                    points=line_points,
                    power=power,
                    feed=feed,
                    dynamic_power=dynamic_power,
                )
                prog += line
    prog.G90()
    prog.G0(X=0, Y=0)
    prog.run()


def xtest_line2(cnc):
    # Init CNC machine, twice, two different ways.
    cnc.run(init())
    init(machine=cnc).run()
    # Line spacing to use.
    line_spacing = 2.5
    # Generate points for a 10mm line
    line_points = gcode.hline(Xf=10)

    # For each of the given powers
    for p, power in enumerate([50, 75, 100, 150, 175, 200, 255]):
        newline = gcode.CNC()
        # Use Absolute coordinates
        newline.G90()
        # Go to a the start of a row, each power has its own row.
        newline.G0(X=0, Y=p * line_spacing)
        # Relative coordinates for each drawn line.
        newline.G91()
        cnc.run(newline)
        # Using and not using dynamic power.
        for d, dynamic_power in enumerate([True, False]):
            # For each of the given feed rates
            for f, feed in enumerate([30, 60, 120, 180, 240, 300]):
                line = gcode.Line(
                    points=line_points,
                    power=power,
                    feed=feed,
                    dynamic_power=dynamic_power,
                )
                print(f"Power: {power}, Feed: {feed}, Dynamic Power: {dynamic_power}")
                cnc.run(line)
    prog.G90()
    prog.G0(X=0, Y=0)
    prog.run()
