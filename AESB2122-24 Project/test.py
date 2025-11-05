import numpy as np
from signals import make_sine, make_square, shift_time, scale_time


def test_make_sine():
    """Test if make_sine generates correct length and type."""
    freq = 5      # Frequency in Hz
    dur = 2       # Duration in seconds
    sr = 100      # Sampling rate in Hz

    sine_wave = make_sine(freq, dur, sr)

    # Basic sanity checks
    assert isinstance(sine_wave, np.ndarray)

    expected_len = sr * dur
    assert len(sine_wave) == expected_len

    print("test_make_sine ran successfully")


def test_make_square():
    """Test if make_square generates only +1 and -1 values."""
    sq_wave = make_square(5, 2, 100)

    # Just to be clear, let's check unique values
    vals = set(np.unique(sq_wave))
    assert vals.issubset({-1.0, 1.0})

    print("test_make_square completed without error")


def test_shift_time():
    """Test that shifting moves samples correctly."""
    original = np.array([1, 2, 3, 4])

    # Shift forward by one sample — 1/4 seconds at 4Hz means 1 sample shift
    shifted = shift_time(original, sec=1/4, sr=4)

    expected = np.array([0, 1, 2, 3])

    assert np.array_equal(shifted, expected)

    print("test_shift_time passed as expected")


def test_scale_time():
    """Test that scale_time stretches or compresses correctly."""
    original = np.array([0, 1, 2, 3])

    # Applying 2x stretch; should double the sample count
    result = scale_time(original, stretch=2)

    assert len(result) == 8

    # Not checking contents yet — just the length for now
    print("test_scale_time ran with expected output length")


if __name__ == "__main__":
    # Basic test runner
    test_make_sine()
    test_make_square()
    test_shift_time()
    test_scale_time()

    print("All tests passed successfully.")
