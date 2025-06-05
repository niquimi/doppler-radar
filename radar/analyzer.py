from scipy.fft import fft, fftfreq
import numpy as np

def analyze_frequency(signal, sample_rate):
    N = len(signal)
    window = np.hanning(N)
    signal_windowed = signal * window  # para reducir el leakage

    yf = fft(signal_windowed)
    xf = fftfreq(N, 1 / sample_rate)

    magnitude = np.abs(yf[:N // 2])
    peak_idx = np.argmax(magnitude)

    # Interpolación parabólica para refinar frecuencia
    if 1 <= peak_idx < len(magnitude) - 1:
        alpha = magnitude[peak_idx - 1]
        beta = magnitude[peak_idx]
        gamma = magnitude[peak_idx + 1]

        p = 0.5 * (alpha - gamma) / (alpha - 2 * beta + gamma)
        freq_interp = xf[peak_idx] + p * (xf[1] - xf[0])
        amp_interp = beta - 0.25 * (alpha - gamma) * p
    else:
        freq_interp = xf[peak_idx]
        amp_interp = magnitude[peak_idx]

    return freq_interp, amp_interp

def calculate_speed(frequency, frequency_emitted, c=343):
    """
    Calculate the speed of the object based on the Doppler shift.

    Parameters:
    frequency (float): Detected frequency in Hz.
    frequency_emitted (float): Emitted frequency in Hz.
    c (float): Speed of sound in m/s (default is 343).

    Returns:
    float: Speed of the object in m/s.
    """
    return c * (frequency - frequency_emitted) / frequency_emitted