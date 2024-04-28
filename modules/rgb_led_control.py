from core.tts import speak_text
from entities.rgb_led import RgbLed

rgb_led = RgbLed(27, 22, 17)

def switch_light(color: str, func):
    speak_text(f'Включаю {color} свет')
    func()

def turn_off():
    speak_text('Выключаю свет')
    rgb_led.turn_off()

def show_colors():
    speak_text('Включаю разные цвета')
    rgb_led.show_colors()

rgb_led_commands = {
    "включи красный свет":    lambda: switch_light('красный', rgb_led.red),
    "включи желтый свет":     lambda: switch_light('желтый', rgb_led.yellow),
    "включи зеленый свет":    lambda: switch_light('зеленый', rgb_led.green),
    "включи голубой свет":    lambda: switch_light('голубой', rgb_led.light_blue),
    "включи фиолетовый свет": lambda: switch_light('фиолетовый', rgb_led.purple),
    "включи белый свет":      lambda: switch_light('белый', rgb_led.white),
    "включи синий свет":      lambda: switch_light('синий', rgb_led.blue),
    'выключи свет': turn_off,
    'включи разные цвета': show_colors,
}