import numpy as np

def generate_sine_wave(frequency, duration, sample_rate):
    """
    Generates a sine wave signal.

    Parameters:
        frequency (float): Frequency of the sine wave in Hz.
        duration (float): Duration of the signal in seconds.
        sample_rate (int): Number of samples per second.

    Returns:
        numpy.ndarray: Array containing the generated sine wave samples.
    """
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    y = np.sin(2 * np.pi * frequency * t)
    return y

