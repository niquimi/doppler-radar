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