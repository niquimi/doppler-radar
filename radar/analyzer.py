from scipy.fft import fft, fftfreq
from scipy.signal import find_peaks
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

def calculate_speed(frequency, f_emitted, c=343):
    """
    Calculate the speed of the object based on the Doppler shift.

    Parameters:
    frequency (float): Detected frequency in Hz.
    frequency_emitted (float): Emitted frequency in Hz.
    c (float): Speed of sound in m/s (default is 343).

    Returns:
    float: Speed of the object in m/s.
    """
    delta_f = frequency - f_emitted
    return (delta_f * c) / (f_emitted)

def analyze_multiple_frequencies(signal, sample_rate, num_peaks=3):
    N = len(signal)
    window = np.hanning(N)
    yf = np.abs(fft(signal * window))[:N // 2]
    xf = fftfreq(N, 1 / sample_rate)[:N // 2]
    yf = yf[:N // 2]  # Solo la mitad positiva del espectro
    # Detectar picos más suavemente
    peaks, properties = find_peaks(yf, height=np.max(yf)*0.05, distance=5)

    # Ordenar por altura (amplitud)
    sorted_peaks = peaks[np.argsort(properties['peak_heights'])[::-1]]

    results = []
    for idx in sorted_peaks[:num_peaks]:
        results.append((xf[idx], yf[idx]))

    return results