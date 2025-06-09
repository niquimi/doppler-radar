import numpy as np

def doppler_shift(frequency, obj_v, c=3e8):
    """
    Calculate the Doppler shift for a moving object.

    Parameters:
    frequency (float): Frequency of the signal in Hz.
    obj_v (float): Velocity of the object in m/s.
    c (float): Speed of light in m/s (default is 3e8).

    Returns:
    float: The Doppler shifted frequency.
    """
    return frequency * (1 + obj_v / c)

def simulate_multiple_objects(f_emit, velocities, amplitudes, c, duration, sample_rate):
    t = np.arange(0, duration, 1/sample_rate)
    signal_total = np.zeros_like(t)

    for v, a in zip(velocities, amplitudes):
        f_shift = f_emit * (1 + v / c)
        signal = a * np.sin(2 * np.pi * f_shift * t)
        signal_total += signal

    return t, signal_total