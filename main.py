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

plot_signals(t, signal, reflected)

# Simulate multiple objects

frequency_emitted = 500
velocities = [50, 20, -30]        # m/s
amplitudes = [1.0, 0.7, 0.5]      # intensidad relativa
c = 343
sample_rate = 50000
duration = 0.1

t, combined_signal = simulate_multiple_objects(frequency_emitted, velocities, amplitudes, c, duration, sample_rate)

frequencies_detected = analyze_multiple_frequencies(combined_signal, sample_rate, num_peaks=3)

plot_spectrum(combined_signal, sample_rate)

for i, (f, amp) in enumerate(frequencies_detected):
    v_est = calculate_speed(frequency_emitted, f, c)
    print(f"[Objeto {i+1}] Frecuencia: {f:.2f} Hz | Δf: {f - frequency_emitted:.2f} Hz | Velocidad estimada: {v_est:.2f} m/s")