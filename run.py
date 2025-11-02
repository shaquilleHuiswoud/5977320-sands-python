from signals import generate_sine_wave

# Parameters
frequency = 5      # Hz
duration = 2       # seconds
sample_rate = 100  # samples per second

# Generate sine wave
sine_wave = generate_sine_wave(frequency, duration, sample_rate)

# Print first 10 samples
print(sine_wave[:10])
