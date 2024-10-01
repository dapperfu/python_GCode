from . import Shapes
from ._version import get_versions
from .Line import hline
from .Line import Line
from .Line import vline
from .GCode import GCode
from .SignalGenerators import sine, cosine, square, sawtooth, triangle

__version__ = get_versions()["version"]
__all__ = ["__version__", "Gcode", "Line", "hline", "vline", "sine", "cosine", "square", "sawtooth", "triangle"]

del get_versions
