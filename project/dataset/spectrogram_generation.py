import matplotlib.pyplot as plt
from scipy import signal
from scipy.io import wavfile
import numpy as np
import random as rd


def generateSpectro(wav_dir):   
    
    sample_rate, samples = wavfile.read(wav_dir)
    frequencies, times, spectrogram = signal.spectrogram(samples, sample_rate)

    plt.pcolormesh(times, frequencies, np.log(spectrogram))
    plt.show()
    plt.savefig(wav_dir + f"{rd.randint(0,1000)}.png")
