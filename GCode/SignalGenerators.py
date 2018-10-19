# -*- coding: utf-8 -*-
"""The math.py module provides very basic functions for signal generation."""

import numpy as np
import scipy.signal


def sine(t, A=1, f=1, phi=0, **kwargs):
    """Generate a sine signal.
    Parameters
    ----------
    t : array_like
        Time vector.
    A : float [1]
        Amplitude.
    f : float [1]
        Frequency. [Hz]
    phi: float [0]
        Phase shift. [rad]
    Returns
    -------
    float
        Sine wave with given amplitude, frequency and phase shift.
    References
    ----------
    A sine wave or sinusoid is a mathematical curve that describes a smooth
    periodic oscillation. A sine wave is a continuous wave. It is named after
    the function sine, of which it is the graph. It occurs often in pure and
    applied mathematics, as well as physics, engineering, signal processing and
    many other fields. Its most basic form as a function of time (t) is[0]:
        y (t) = A*sin(2πf*t + φ)
    
    In mathematics, the sine is a trigonometric function of an angle. The sine
    of an acute angle is defined in the context of a right triangle: for the
    specified angle, it is the ratio of the length of the side that is opposite
    that angle to the length of the longest side of the triangle (the hypotenuse).
    More generally, the definition of sine (and other trigonometric functions)
    can be extended to any real value in terms of the length of a certain line
    segment in a unit circle. More modern definitions express the sine as an
    infinite series or as the solution of certain differential equations,
    allowing their extension to arbitrary positive and negative values and even
    to complex numbers.[1]
    [0]. https://en.wikipedia.org/wiki/Sine_wave
    [1]. https://en.wikipedia.org/wiki/Sine
    """
    sine_ = A * np.sin(2 * np.pi * f * t + phi, **kwargs)
    return sine_


sin = sine


def cosine(t, A=1, f=1, **kwargs):
    """Generate a cosine signal.
    Parameters
    ----------
    t : array_like
        Time vector.
    A : float [1]
        Amplitude.
    f : float [1]
        Frequency. [Hz]
    Returns
    -------
    float
        Cosine wave with given amplitude and frequency.
    """
    cosine_ = A * np.sin(2 * np.pi * f * t)
    return cosine_


cos = cosine


def square(t, A=1, f=1, **kwargs):
    """Generate a square signal.
    Parameters
    ----------
    t : array_like
        Time vector.
    A : float [1]
        Amplitude.
    f : float [1]
        Frequency. [Hz]
    Returns
    -------
    float
        Square wave with given amplitude and frequency.
    """
    square_ = A * scipy.signal.square(2 * np.pi * f * t)
    return square_


sq = square


def sawtooth(t, A=1, f=1, **kwargs):
    """Generate a sawtooth signal.
    Parameters
    ----------
    t : array_like
        Time vector.
    A : float [1]
        Amplitude.
    f : float [1]
        Frequency. [Hz]
    Returns
    -------
    float
        Sawtooth wave with given amplitude and frequency.
    """
    sawtooth_ = A * scipy.signal.sawtooth(2 * np.pi * f * t, width=1)
    return sawtooth_


saw = sawtooth


def triangle(t, A=1, f=1, **kwargs):
    """Generate a triangle signal.
    Parameters
    ----------
    t : array_like
        Time vector.
    A : float [1]
        Amplitude.
    f : float [1]
        Frequency. [Hz]
    Returns
    -------
    float
        Triangle wave with given amplitude and frequency.
    """
    triangle_ = A * scipy.signal.sawtooth(2 * np.pi * f * t, width=0.5)
    return triangle_


tri = triangle


def pwm(t, A=1, f=1, duty_cycle=0.5, **kwargs):
    """Generate a PWM signal.
    Note: PWM is positive only. [0, Amplitude]
    Parameters
    ----------
    t : array_like
        Time vector.
    A : float [1]
        Amplitude.
    f : float [1]
        Frequency. [Hz]
    duty_cycle: float [0.5]
        Duty Cycle [Unitless]
    Returns
    -------
    float
        PWM signal with given amplitude, frequency and duty cycle.
    """
    pwm_ = A * scipy.signal.square(t=2 * np.pi * f * t, duty=duty_cycle)
    pwm_[pwm_ < 0] = 0
    return pwm_
    
def step(t=None, step_time=None, initial_value=None, final_value=None, amplitude=None, **kwargs):
    """Generate a step at given time.
    
    Parameters
    ----------
    t : array_like
        Time vector.
    step_time: float [1]
        Time to step.
    initial_value: float [0]
        Initial value before step time.
    final_value: float [1]
        Final value after step time.
    Returns
    -------
    float
        Step signal with given values.
    """
    if t is None:
    
    if A is not None:
        final_value=A
        initial_value=0
    t = np.array(t)
    out = np.heaviside(t-step_time, final_value)
    out[out==0] = initial_value
    out[out==1] = final_value
	return out
