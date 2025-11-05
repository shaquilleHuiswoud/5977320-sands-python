# Signal Processing Tools

A Python package for generating, modifying, and visualizing basic signals.  
Developed as part of the AESB2122-24 Signals & Systems project of Applied Earth Science at TU Delft.

The project contains:
- Code that creates basic signals (sine and square waves)
- Tools for shifting signals in time and stretching or compressing them
- A script that visualizes original vs. modified signals
- A small set of tests to verify that the functions behave correctly

---

## What This Code Does

### Creating Signals
The `signals.py` file provides functions that return NumPy arrays:
- **make_sine(...)** creates a continuous sine wave
- **make_square(...)** produces a binary (+1 / -1) square wave

### Changing Signals
Two operations are included:
- **shift_time(...)** moves a signal forward or backward in time  
  (delay = positive shift, advance = negative shift)
- **scale_time(...)** stretches or compresses a signal by interpolation

---

## Example Output

Running the included script will generate two images:

sine_wave.png
square_wave.png

Each image displays:
- The original signal
- The time-shifted version
- The time-scaled version

---

## Running the Code
python run.py
This prints a few sample values to the terminal and saves the figures as PNG files.

---

## Testing

A separate file (`test.py`) includes basic checks to ensure that:
- Sine wave has the correct number of samples
- Square wave contains only +1 and -1 values
- Shifting does not change signal length
- Time scaling produces the correct new length

Run tests with:
python test.py
---

## Requirements

- Python 3
- NumPy
- Matplotlib

(These are listed in `pyproject.toml`)

Install manually if needed:
pip install numpy matplotlib


---

## Project Structure
