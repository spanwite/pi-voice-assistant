from gtts import gTTS
import os
import platform

def play_audio(file):
    system = platform.system()

    if system == "Windows":
        os.system(f'start {file}')
    elif system == 'Linux':
        os.system(f'mpg123 {file} 2>/dev/null')

    print(system)


def speak_text(text, lang='ru'):
    tts = gTTS(text=text, lang=lang)

    audio_file = 'output.mp3'

    tts.save(audio_file)
    play_audio(audio_file)