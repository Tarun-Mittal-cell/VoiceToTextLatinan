import numpy as np
import wave
import struct

sample_rate = 44100.0
duration = 5.0  # in seconds
frequency = 440.0  # A4 note

t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
y = 0.5 * np.sin(2 * np.pi * frequency * t)

with wave.open("sine_wave.wav", "w") as wf:
    wf.setnchannels(1)
    wf.setsampwidth(2)
    wf.setframerate(sample_rate)
    for sample in y:
        wf.writeframesraw(struct.pack("<h", int(sample * 32767.0)))

print("File 'sine_wave.wav' generated.")
