import numpy as np

def generate_signal(frequency, duration, sample_rate):
    """
    Generate a sinusoidal signal for Doppler radar simulation.

    Parameters:
    frequency (float): Frequency of the signal in Hz.
    duration (float): Duration of the signal in seconds.
    sample_rate (int): Number of samples per second.

    Returns:
    tuple: A tuple containing:
        - np.ndarray: Time vector.
    np.ndarray: Array containing the generated signal.
    """
    t = np.arange(0, duration, 1/sample_rate)
    signal = np.sin(2 * np.pi * frequency * t)
    return t, signal