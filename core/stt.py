import speech_recognition as sr

r = sr.Recognizer()

def recognize_speech() -> tuple[str, str]:
    text, error = '', ''

    with sr.Microphone(sample_rate=8000) as source:
        r.adjust_for_ambient_noise(source)
        audio_data = r.listen(source,phrase_time_limit=4)
        
    try:
        text = r.recognize_google(audio_data, language="ru-RU")
    except sr.UnknownValueError:
        error = "не удалось распознать речь"
    except sr.RequestError as e:
        error = "не удалось отправить запрос на сервер или получить ответ"

    if not text and not error:
        error = "распознанный текст является пустой строкой"

    return (text, error)