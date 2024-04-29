from assistant import VoiceAssistant
from modules.rgb_led import rgb_led_commands

va = VoiceAssistant()

va.add_commands(rgb_led_commands)
va.start()