import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq
import numpy as np

def plot_signals(t, original, shifted):
    plt.plot(t, original, label='Original Signal', color='blue')
    plt.plot(t, shifted, label='Reflected', color='red')
    plt.legend()
    plt.title('Doppler Shifted Signals')
    plt.show()

def plot_spectrum(signal, sample_rate):
    N = len(signal)
    window = np.hanning(N)
    yf = np.abs(fft(signal * window))[:N//2]
    xf = fftfreq(N, 1 / sample_rate)[:N//2]

    plt.figure(figsize=(10, 4))
    plt.plot(xf, yf)
    plt.title("Espectro de frecuencias (FFT)")
    plt.xlabel("Frecuencia (Hz)")
    plt.ylabel("Amplitud")
    plt.grid(True)
    plt.show()