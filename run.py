import matplotlib.pyplot as plt
from signals import generate_sine_wave

# Parameters
frequency = 5      # Hz
duration = 2       # seconds
sample_rate = 100  # samples per second

# Generate sine wave
sine_wave = generate_sine_wave(frequency, duration, sample_rate)

# Create time axis for plotting
t = [i / sample_rate for i in range(len(sine_wave))]

# Plot the sine wave
plt.plot(t, sine_wave)
plt.title("5 Hz Sine Wave")
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.grid(True)
plt.show()
