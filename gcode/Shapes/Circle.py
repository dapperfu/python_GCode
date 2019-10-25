# -*- coding: utf-8 -*-
import numpy as np

from ..GCode import GCode


class Circle(GCode):
    def __init__(self, center=(0, 0), radius=10, clockwise=True, *args, **kwargs):
        self.center = center
        self.radius = radius
        self.clockwise = clockwise
        self.laser_power = 1
        self.dynamic_power = True

        super().__init__(*args, **kwargs)

    def generate_gcode(self):
        self.buffer = list()
        center_x, center_y = self.center
        self.G0(X=(center_x - self.radius), Y=(center_y))
        if self.dynamic_power:
            self.M4(S=self.laser_power)
        else:
            self.M3(S=self.laser_power)
        arg_cfg = {
            "X": (center_x - self.radius),
            "Y": (center_y),
            "I": (self.radius),
            "J": 0,
        }
        if self.clockwise:
            self.G2(**arg_cfg)
        else:
            self.G3(**arg_cfg)
        self.M5()

    @property
    def _cls(self):
        return self.__class__.__name__

    def __repr__(self):
        return f"{self._cls}<O={self.center}, R={self.radius}>"
