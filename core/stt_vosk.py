import pyaudio
import sounddevice
from core.tts import speak_text
import json
from vosk import Model, KaldiRecognizer

def recognize_speech(model_path: str, callback, blocksize = 512, samplerate = 16000):
    model = Model(model_path)
    rec = KaldiRecognizer(model, samplerate)

    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16, channels=1, rate=samplerate, input=True, frames_per_buffer=blocksize)

    speak_text('Ассистент запущен и готов выполнять ваши команды')

    while True:
        data = stream.read(blocksize)
        if len(data) == 0:
            break
        if rec.AcceptWaveform(data):
            callback(json.loads(rec.Result())["text"])

    stream.stop_stream()
    stream.close()
    p.terminate()