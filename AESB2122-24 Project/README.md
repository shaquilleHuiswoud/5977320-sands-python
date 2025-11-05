# Signal Processing Tools

A Python package for generating, modifying, and visualizing basic signals.  
Developed as part of the AESB2122-24 Signals & Systems project in Applied Earth Science at TU Delft.

---

## Overview

This project includes tools for:

- Creating simple signals like sine and square waves  
- Modifying signals by shifting or scaling them in time  
- Visualizing the original vs. modified signals  
- Running a few basic tests to make sure the core functions work properly

---

## What This Code Does

### Creating Signals

Inside `signals.py`, you'll find two functions that return NumPy arrays:

- `make_sine(freq, duration, sr)`  
  Generates a sine wave with the specified frequency, duration, and sampling rate.

- `make_square(freq, duration, sr)`  
  Produces a square wave that alternates between +1 and -1.

### Changing Signals

There are two key signal transformations included:

- `shift_time(signal, sec, sr)`  
  Shifts the signal forward or backward by a number of seconds.  
  (Use positive values for delays, negative for advancing.)

- `scale_time(signal, stretch)`  
  Stretches or compresses the signal in time using interpolation.

---

## Example Output

Running the script will generate two PNG image files:

- `sine_wave.png`
- `square_wave.png`

Each image shows:

- The original signal
- A version shifted in time
- A version scaled in time

---

## How to Run It

To generate the signals and save the plots:

python run.py


This will print out some sample values and save the images to the current folder.

---

## Testing

A separate file `test.py` includes some basic checks:

- Sine wave has the expected number of samples  
- Square wave contains only +1 and -1 values  
- Time shifting does not change the signal length  
- Scaling updates the signal length as expected

To run the tests:

python test.py


---

## Requirements

This project requires:

- Python 3
- NumPy
- Matplotlib

These are listed in `pyproject.toml`, but you can also install them manually:

pip install numpy matplotlib


---

## Project Structure

AESB2122-24 Project/
│
├── README.md            # Project description and usage instructions
├── hello.py             # (Possibly a sample script or placeholder)
├── main.py              # Main logic or entry point (if used)
├── pyproject.toml       # Project metadata and dependencies
├── run.py               # Script to generate and save signal plots
├── signals.py           # Functions to create and modify signals
├── test.py              # Basic unit tests for signal functions
├── __pycache__/         # Auto-generated Python bytecode cache