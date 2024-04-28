import speech_recognition as sr

r = sr.Recognizer()

def recognize_speech() -> tuple[str, str]:
    text, error = '', ''

    with sr.Microphone(sample_rate=18000) as source:
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        audio_data = r.listen(source)
        
    try:
        text = r.recognize_google(audio_data, language="ru-RU")
    except sr.UnknownValueError:
        error = "не удалось распознать речь"
    except sr.RequestError as e:
        error = "ошибка сервиса распознавания речи; {0}".format(e)

    return (text, error)