from . import Shapes
from ._version import get_versions
from .Line import hline
from .Line import Line
from .Line import vline
from .GCode import GCode

__version__ = get_versions()["version"]
__all__ = ["__version__", "Gcode", "Line", "hline", "vline"]

del get_versions
