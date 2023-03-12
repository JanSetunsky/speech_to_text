import threading
import speech_recognition as sr
import json
import pyaudio
import keyboard

r = sr.Recognizer()
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, frames_per_buffer=1024)

def record_audio():
    frames = []
    while True:
        data = stream.read(1024)
        frames.append(data)
        if keyboard.is_pressed('esc'):
            stream.stop_stream()
            stream.close()
            p.terminate()
            audio = sr.AudioData(b''.join(frames), 44100, 2)
            recognized_text = recognize_speech(audio)
            print('{'+"'text':'{}'".format(recognized_text)+'}')
            break

def recognize_speech(audio):
    try:
        recognized_text = r.recognize_google(audio, language='cs-CZ')
        return recognized_text
    except sr.UnknownValueError:
        return None
    except sr.RequestError as e:
        print("Chyba při připojení k internetu; {0}".format(e))
        return None

t = threading.Thread(target=record_audio)
t.start()