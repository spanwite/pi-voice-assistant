from rapidfuzz import fuzz
from core.stt import recognize_speech
from core.tts import speak_text
from modules.rgb_led_control import rgb_led_commands
import sounddevice

all_commands = dict()
all_commands.update(rgb_led_commands)

assistant_name = 'ассистент'
should_do_command = False

def do_command(text: str):
    global should_do_command
    best_match = max(all_commands.keys(), key=lambda x: fuzz.ratio(text, x))
    percent = fuzz.ratio(text, best_match)

    if percent > 70:
        all_commands[best_match]()
        should_do_command = True
    elif percent >= 50:
        should_do_command = True
    else:
        should_do_command = False

    print(best_match, percent)

speak_text('Ассистент запущен и готов выполнять ваши команды')

while True:
    text, error = recognize_speech()
 
    if error:
        print(f'Ошибка: "{error}"')
        continue

    print(f'Распознано: "{text}"')

    if assistant_name in text:
        should_do_command = True
        speak_text('Я слушаю вашу команду')
        continue

    if not should_do_command:
        continue

    do_command(text.lower())