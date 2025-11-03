"""
signals.py
----------
Basic code for signal generation and editing tools for the signal.
Author: Shaquille Huiswoud
"""

import numpy as np


def make_sine(freq: float, dur: float, sr: int) -> np.ndarray:
    """
    Generate a sine wave.

    freq: cycles per second (Hz)
    dur: how long it lasts (seconds)
    sr: samples per second

    Returns: NumPy array of the wave
    """
    t_axis = np.linspace(0, dur, int(sr * dur), endpoint=False)
    return np.sin(2 * np.pi * freq * t_axis)


def make_square(freq: float, dur: float, sr: int) -> np.ndarray:
    """
    Generate a square wave (±1 values).

    freq: Hz
    dur: seconds
    sr: sample rate

    Returns: NumPy array of square wave
    """
    t = np.linspace(0, dur, int(sr * dur), endpoint=False)
    phase = (freq * t) % 1.0
    return np.where(phase < 0.5, 1.0, -1.0)


def shift_time(sig: np.ndarray, sec: float, sr: int) -> np.ndarray:
    """
    Shift signal in time (±seconds).

    Positive: delay
    Negative: advance

    Returns: shifted version, same length
    """
    shift_samples = int(sec * sr)
    shifted = np.zeros_like(sig)

    if shift_samples > 0:
        shifted[shift_samples:] = sig[:-shift_samples]
    elif shift_samples < 0:
        shifted[:shift_samples] = sig[-shift_samples:]
    else:
        shifted[:] = sig

    return shifted


def scale_time(signal_data: np.ndarray, stretch: float) -> np.ndarray:
    """
    Stretch/compress time.

    >1 = slower
    <1 = faster

    Returns: rescaled signal using interpolation
    """
    if stretch <= 0.0:
        raise ValueError("Scaling factor should be > 0")

    new_len = max(1, int(len(signal_data) * stretch))
    old_x = np.arange(len(signal_data))
    new_x = np.linspace(0, len(signal_data) - 1, new_len)

    return np.interp(new_x, old_x, signal_data)
