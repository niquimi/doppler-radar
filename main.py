from radar.signal_generator import generate_signal
from radar.object_simulation import doppler_shift
from radar.analyzer import analyze_frequency, calculate_speed
from visualizations.plots import plot_signals

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