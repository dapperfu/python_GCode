import pytest

import gcode


@pytest.mark.parametrize(
    "shape", [gcode.Line, gcode.Shapes.Square, gcode.Shapes.Circle]
)
def test_shape_defaults(shape):
    print(shape())
