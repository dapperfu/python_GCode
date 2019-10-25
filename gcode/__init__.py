from . import Shapes
from ._version import get_versions
from .GCode import GCode
from .Line import hline
from .Line import Line
from .Line import vline

__version__ = get_versions()["version"]
__all__ = ["__version__", "Gcode", "Shapes", "Line"]

del get_versions
