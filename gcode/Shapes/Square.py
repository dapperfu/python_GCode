# -*- coding: utf-8 -*-
import numpy as np

from ..Line import Line


class Square(Line):
    def __init__(self, side: float = 10.0, origin=np.array([0, 0]), *args, **kwargs):
        self.side = side
        self.origin = origin

        kwargs["points"] = self._points

        super().__init__(*args, **kwargs)

    @property
    def _points(self):
        return np.array(
            [
                [self.origin[0], self.origin[1]],
                [self.origin[0] + self.side, self.origin[1]],
                [self.origin[0] + self.side, self.origin[1] + self.side],
                [self.origin[0], self.origin[1] + self.side],
                [self.origin[0], self.origin[1]],
            ]
        )

    def generate_gcode(self):
        self.points = self._points
        super().generate_gcode()

    @property
    def _cls(self):
        return self.__class__.__name__

    def __repr__(self):
        return f"{self._cls}<O={self.origin}, L={self.side}>"
