import wave
import sys
import os
import pyaudio
CHUNK = 1024
if sys.platform[0] == 'l':
    path = "/home/jan/git/PlaySound"
if sys.platform[0] == 'w':
    path = "C:/Users/janbo/OneDrive/Documents/GitHub/PlaySound"
os.chdir(path)
filename = "WAV/failure.wav"
with wave.open(filename, 'rb') as wf:
    p = pyaudio.PyAudio()
    try:
        stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),channels=wf.getnchannels(),rate=wf.getframerate(),output=True)
    except Exception as error:
        print("Can not open stream", error)
    while len(data := wf.readframes(CHUNK)): 
        stream.write(data)
    stream.close()
    p.terminate()
filename = "WAV/success.wav"
with wave.open(filename, 'rb') as wf:
    p = pyaudio.PyAudio()
    try:
        stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),channels=wf.getnchannels(),rate=wf.getframerate(),output=True)
    except Exception as error:
        print("Can not open stream", error)
    while len(data := wf.readframes(CHUNK)): 
        stream.write(data)
    stream.close()
    p.terminate()
key = input("Wait")
