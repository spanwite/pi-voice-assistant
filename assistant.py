from rapidfuzz import fuzz
from core.stt import recognize_speech
from core.tts import speak_text
from modules.rgb_led_control import rgb_led_commands
import sounddevice

all_commands = dict()
all_commands.update(rgb_led_commands)

def recognize_command(command: str):
    best_match = max(all_commands.keys(), key=lambda x: fuzz.partial_ratio(command, x))
    percent = fuzz.partial_ratio(command, best_match)

    if percent > 70:
        all_commands[best_match]()

    print(best_match, fuzz.partial_ratio(command, best_match))

speak_text('Ассистент запущен и готов выполнять ваши команды')

while True:
    text, error = recognize_speech()
 
    if error:
        print(f'Ошибка: "{error}"')
        continue

    if not text:
        print('Пустой текст')

    print(f'Распознано: "{text}"')

    recognize_command(text.lower())