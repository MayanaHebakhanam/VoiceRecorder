#This Python module provides bindings for the PortAudio library and a few convenience functions
# to play and record NumPy arrays containing audio signals.
import sounddevice
#SciPy has many modules, classes, and functions available to read data from and write data to a
# variety of file formats.
from scipy.io.wavfile import write

#Sampling rate or sampling frequency defines the number of samples per second (or per other unit) taken from a
# continuous signal to make a discrete or digital signal.
#samplerate
fs=44100
second=int(input("Enter the time duration in seconds:"))
print("Recording......\n")
# Channel parameter indicates Number of channels to record.
record_voice=sounddevice.rec(int(second*fs),samplerate=fs,channels=2)
sounddevice.wait()
write("out.wav",fs,record_voice)
print("Finished....\nPlease Check it...")
