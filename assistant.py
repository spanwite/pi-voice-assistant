from rapidfuzz import fuzz
from core.stt import recognize_speech
from core.tts import speak_text
import sounddevice

class VoiceAssistant:
    all_commands = dict()
    should_do_command = True
    
    def __init__(self, name: str):
        self.name = name

    def add_commands(self, commands: object):
        self.all_commands.update(commands)

    def do_command(self, text: str):
        best_match = max(self.all_commands.keys(), key=lambda x: fuzz.ratio(text, x))
        percent = fuzz.ratio(text, best_match)

        if percent > 70:
            self.all_commands[best_match]()
            self.should_do_command = True
        elif percent > 50:
            self.should_do_command = True
        else:
            self.should_do_command = False

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

            print(f'Распознано: "{text}"')

            if self.name in text:
                self.should_do_command = True
                speak_text('Я слушаю вашу команду')
                continue

            if not self.should_do_command:
                continue

            self.do_command(text.lower())