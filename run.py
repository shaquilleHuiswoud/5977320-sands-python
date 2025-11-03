"""
run.py
------
This script is used to generate the sine and square wave signals from signals.py file, it applies time-based transformations
such as shifting and scaling, and visualizes the results using plots.

It uses helper functions from the signals.py to perform signal creation and manipulation,
then saves comparison plots showing the original and modified signals.

Author: Shaquille Huiswoud
"""

import numpy as np
import matplotlib.pyplot as plt
from signals import make_sine, make_square, shift_time, scale_time


def plot_and_save(t, y_orig, y_shifted, y_scaled, label_prefix: str, out_file: str, sample_rate: int):
    """
    Plot the original, time-shifted, and time-scaled versions of a signal,
    and save the result as a PNG image.

    Parameters:
    - t: Time axis for the original and shifted signals
    - y_orig: Original signal
    - y_shifted: Time-shifted version of the signal
    - y_scaled: Time-scaled (stretched or compressed) version of the signal
    - label_prefix: Used in the plot title to label the signal type
    - out_file: Filename for saving the output image
    - sample_rate: Sampling rate used to recalculate time for the scaled signal
    """
    t_scaled = np.arange(len(y_scaled)) / sample_rate

    plt.figure(figsize=(9.5, 6))
    plt.plot(t, y_orig, label="Original", lw=1.5)
    plt.plot(t, y_shifted, label="Shifted", lw=1.2)
    plt.plot(t_scaled, y_scaled, label="Time-Scaled", lw=1.2)

    plt.title(f"{label_prefix} - Comparison View")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.legend(loc="upper right")
    plt.grid(True, linestyle='--', alpha=0.25)
    plt.tight_layout()

    plt.savefig(out_file, dpi=144)
    print(f"Plot saved to file: {out_file}")
    plt.close()


def main():
    """
    Main execution function. It sets the signal parameters,
    generates sine and square waves, applies time shifting and scaling,
    and plots the results for analysis.
    """
    # Signal configuration
    frequency = 5.0         # Frequency in Hz
    duration = 2.0          # Duration of signal in seconds
    sample_rate = 100       # Sampling rate in samples per second

    # Time transformation parameters
    delay_seconds = 0.3     # Time shift (positive = delay, negative = advance)
    scale_factor = 1.5      # Time scale factor (>1 = stretch, <1 = compress)

    # Generate sine wave and its time axis
    sine_wave = make_sine(frequency, duration, sample_rate)
    t = np.arange(len(sine_wave)) / sample_rate

    # Apply transformations to sine wave
    sine_shifted = shift_time(sine_wave, sec=delay_seconds, sr=sample_rate)
    sine_scaled = scale_time(sine_wave, stretch=scale_factor)

    # Plot and save results for sine wave
    plot_and_save(t, sine_wave, sine_shifted, sine_scaled,
                  label_prefix="Sine Wave",
                  out_file="sine_wave.png",
                  sample_rate=sample_rate)

    # Generate square wave and apply the same transformations
    square_wave = make_square(frequency, duration, sample_rate)
    square_shifted = shift_time(square_wave, sec=delay_seconds, sr=sample_rate)
    square_scaled = scale_time(square_wave, stretch=scale_factor)

    # Plot and save results for square wave
    plot_and_save(t, square_wave, square_shifted, square_scaled,
                  label_prefix="Square Wave",
                  out_file="square_wave.png",
                  sample_rate=sample_rate)

    # Print the first 10 samples for inspection
    print("Sine head (10):", sine_wave[:10])
    print("Square head (10):", square_wave[:10])


if __name__ == "__main__":
    main()
