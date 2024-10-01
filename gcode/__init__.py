from . import Shapes
from ._version import get_versions
from .GCode import GCode
from .Line import hline
from .Line import Line
from .Line import vline
from .SignalGenerators import cosine
from .SignalGenerators import sawtooth
from .SignalGenerators import sine
from .SignalGenerators import square
from .SignalGenerators import triangle

__version__ = get_versions()["version"]
__all__ = [
    "__version__",
    "Gcode",
    "Line",
    "hline",
    "vline",
    "sine",
    "cosine",
    "square",
    "sawtooth",
    "triangle",
]

del get_versions
