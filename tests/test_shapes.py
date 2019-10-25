import pytest

import gcode


@pytest.mark.parametrize("shape", [gcode.Shapes.Square, gcode.Shapes.Circle])
def test_shape_defaults(shape):
    print(shape())
