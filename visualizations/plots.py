import matplotlib.pyplot as plt

def plot_signals(t, original, shifted):
    plt.plot(t, original, label='Original Signal', color='blue')
    plt.plot(t, shifted, label='Reflected', color='red')
    plt.legend()
    plt.title('Doppler Shifted Signals')
    plt.show()