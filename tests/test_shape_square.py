import pytest

import gcode


@pytest.mark.parametrize("side", [1, 5, 10])
def test_square_side(side):
    print(gcode.Shapes.Square(side=side))


@pytest.mark.parametrize("origin", [(0, 0), (5, 0), (0, 10)])
def test_square_origin(origin):
    print(gcode.Shapes.Square(origin=origin))


@pytest.mark.parametrize("side", [1, 5, 10])
@pytest.mark.parametrize("origin", [(0, 0), (5, 0), (0, 10)])
def test_square_side_origin(side, origin):
    print(gcode.Shapes.Square(side=side, origin=origin))


@pytest.mark.parametrize("laser_power", [1, 128, 255])
def test_square_power(laser_power):
    print(gcode.Shapes.Square(power=laser_power))


@pytest.mark.parametrize("laser_power", [128, 255])
def test_square_power_change(laser_power):
    print(f"# Default Square")
    square = gcode.Shapes.Square()
    print(square)
    square.power = laser_power
    print(f"# Changing Power to {laser_power}")
    print(square)
