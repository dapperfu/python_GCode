# -*- coding: utf-8 -*-
import numpy as np
import scipy as sp


import numpy as np
from typing import Union

def sine(t: Union[float, np.ndarray], A: float = 1, f: float = 1, phi: float = 0, D: float = 0) -> Union[float, np.ndarray]:
    """
    Compute the sine wave.

    Parameters
    ----------
    t : float or numpy.ndarray
        Time variable.
    A : float, optional
        Amplitude of the sine wave, the peak deviation from zero. Default is 1.
    f : float, optional
        Frequency of the sine wave in Hertz (cycles per second). Default is 1.
    phi : float, optional
        Phase shift in radians. Default is 0.
    D : float, optional
        Vertical shift (DC offset). Default is 0.

    Returns
    -------
    float or numpy.ndarray
        The computed sine wave at time `t`.
    """
    return A * np.sin(2 * np.pi * f * t + phi) + D

def cosine(t: Union[float, np.ndarray], A: float = 1, f: float = 1, phi: float = 0, D: float = 0) -> Union[float, np.ndarray]:
    """
    Compute the cosine wave.

    Parameters
    ----------
    t : float or numpy.ndarray
        Time variable.
    A : float, optional
        Amplitude of the cosine wave, the peak deviation from zero. Default is 1.
    f : float, optional
        Frequency of the cosine wave in Hertz (cycles per second). Default is 1.
    phi : float, optional
        Phase shift in radians. Default is 0.
    D : float, optional
        Vertical shift (DC offset). Default is 0.

    Returns
    -------
    float or numpy.ndarray
        The computed cosine wave at time `t`.
    """
    return A * np.cos(2 * np.pi * f * t + phi) + D

def square(t, A=1, f=1, phi=0, D=0):
    """
    t: time
    A: the amplitude, the peak deviation of the function from zero.
    f: the ordinary frequency, the number of oscillations (cycles) that occur each second of time.
    D: non-zero center amplitude
    """
    square_ = A * sp.signal.square(2 * np.pi * f * t+phi) + D
    return square_


def sawtooth(t, A=1, f=1, D=0):
    """
    t: time
    A: the amplitude, the peak deviation of the function from zero.
    f: the ordinary frequency, the number of oscillations (cycles) that occur each second of time.
    D: non-zero center amplitude
    """
    sawtooth_ = A * sp.signal.sawtooth(2 * np.pi * f * t, width=1) + D
    return sawtooth_


def triangle(t, A=1, f=1, D=0):
    """
    t: time
    A: the amplitude, the peak deviation of the function from zero.
    f: the ordinary frequency, the number of oscillations (cycles) that occur each second of time.
    D: non-zero center amplitude
    """
    triangle_ = A * sp.signal.sawtooth(2 * np.pi * f * t, width=0.5) + D
    return triangle_


signal_generators = [sine, cosine, square, sawtooth, triangle]
