from rapidfuzz import fuzz
from core.stt import recognize_speech
from core.tts import speak_text
import sounddevice

class VoiceAssistant:
    all_commands = dict()

    def add_commands(self, commands: object):
        self.all_commands.update(commands)

    def do_command(self, text: str):
        best_match = max(self.all_commands.keys(), key=lambda x: fuzz.ratio(text, x))
        percent = fuzz.ratio(text, best_match)

        if percent > 70:
            self.all_commands[best_match]()

        print(best_match, percent)

    def start(self):
        speak_text('Ассистент запущен и готов выполнять ваши команды')
        
        while True:
            try:
                text, error = recognize_speech()
            except KeyboardInterrupt:
                break

            if error:
                print(f'Ошибка: "{error}"')
                continue

            if 'ассистент' in text:
                speak_text('Я слушаю вашу команду')
                continue

            print(f'Распознано: "{text}"')

            self.do_command(text.lower())