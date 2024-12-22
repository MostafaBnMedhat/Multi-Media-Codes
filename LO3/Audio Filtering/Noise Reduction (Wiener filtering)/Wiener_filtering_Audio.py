import numpy as np
import  scipy.io.wavfile as  wavfile
from  scipy.signal import wiener

fs , noisy_audio = wavfile.read('noisy_audio_Final.wav')
noisy_audio = noisy_audio/np.max(np.abs(noisy_audio))

filtered_audio= wiener(noisy_audio)
filtered_audio = (filtered_audio * 32767).astype(np.int16)
wavfile.write('filtered_audio.wav',fs,filtered_audio)
