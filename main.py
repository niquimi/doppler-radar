import time
import numpy as np
from radar.signal_generator import generate_signal
from radar.object_simulation import doppler_shift, simulate_multiple_objects
from radar.analyzer import analyze_frequency, calculate_speed, analyze_multiple_frequencies
from visualizations.plots import plot_signals, plot_spectrum


f_emitted = 500  # 24 GHz typical for radar
v_obj = 50
c = 343
sample_rate = 50000  # 1 MHz
duration = 0.05

t, signal = generate_signal(f_emitted, duration, sample_rate)

f_shifted = doppler_shift(f_emitted, v_obj, c)
_, reflected = generate_signal(f_shifted, duration, sample_rate)

# Analyze the original and shifted signals
f_detected, amplitude = analyze_frequency(reflected, sample_rate)
print(f"Frecuencia detectada: {f_detected:.2f} Hz")
print(f"Delta f: {f_detected - f_emitted:.2f} Hz")

print(f"Velocidad estimada del objeto: {calculate_speed(f_detected, f_emitted, c):.2f} m/s")

#plot_signals(t, signal, reflected)

# Simulate multiple objects

frequency_emitted = 24000
# Valores reales
vel_real = [50, 20, -30]
amplitudes = [1.0, 0.7, 0.5]      # intensidad relativa
c = 343
sample_rate = 100000
duration = 0.2

f_shifted_real = [doppler_shift(frequency_emitted, v, c) for v in vel_real]
print("\nComparación real:")
for i, (f_real, v_real) in enumerate(zip(f_shifted_real, vel_real)):
    print(f"Real Objeto {i+1}: f = {f_real:.2f} Hz | v = {v_real} m/s")

t, combined_signal = simulate_multiple_objects(frequency_emitted, vel_real, amplitudes, c, duration, sample_rate)

frequencies_detected = analyze_multiple_frequencies(combined_signal, sample_rate, num_peaks=3)

plot_spectrum(combined_signal, sample_rate)

used = set()
for i, (f_detected, _) in enumerate(frequencies_detected):
    best_match = None
    min_diff = float('inf')
    for j, f_true in enumerate(f_shifted_real):
        if j in used:
            continue
        diff = abs(f_true - f_detected)
        if diff < min_diff:
            min_diff = diff
            best_match = j
    used.add(best_match)
    v_est = calculate_speed( f_detected, frequency_emitted, c)
    print(f"[Detectado {i+1}] f = {f_detected:.2f} Hz | Δf = {f_detected - frequency_emitted:.2f} Hz | v_est = {v_est:.2f} m/s ≈ Real: {vel_real[best_match]} m/s")