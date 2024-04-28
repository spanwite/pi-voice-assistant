from gtts import gTTS
from playsound import playsound
import os

def speak_text(text, lang='ru'):
    tts = gTTS(text=text, lang=lang)

    project_root = os.path.abspath(os.curdir)
    audio_file = os.path.join(project_root, 'output.mp3')

    tts.save(audio_file)
    playsound(audio_file)
    os.remove(audio_file)