import pyttsx3
import speech_recognition as sr


def detect_language(word: str):
    ru = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    en = 'abcdefghijklmnopqrstuvwxyz'
    c_ru = 0
    c_en = 0
    for char in word.lower():
        if char in ru:
            c_ru += 1
        elif char in en:
            c_en += 1
    if c_ru == c_en == 0:
        return 'oth'
    if c_ru < c_en:
        return 'en'
    else:
        return 'ru'


def speak(_text):
    if not _text:
        return _text
    engine = pyttsx3.init()
    v = engine.getProperty('voices')
    v = {
        'ru': v[0].id,
        'en': v[1].id
    }

    text = _text.split()
    text = [[x, detect_language(x)] for x in text]
    res = [text[0]]
    for word in text[1:]:
        if word[1] != 'oth' and res[-1][1] == 'oth':
            res[-1][1] = word[1]
        if word[1] == res[-1][1] or word[1] == 'oth':
            res[-1][0] += f' {word[0]}'
        else:
            res.append(word)
    del text

    for piece in res:
        engine.setProperty('voice', v[piece[1]])
        engine.say(piece[0])
        engine.runAndWait()

    del engine
    return _text


def recognise():
    r = sr.Recognizer()
    mic = sr.Microphone()
    text = ''
    with mic as source:
        # r.adjust_for_ambient_noise(source, 3)
        r.dynamic_energy_threshold = True
        print("Listening")
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio, language="ru-RU").lower()
    except sr.UnknownValueError:
        print("Невозможно расползнать голос")
    except sr.RequestError as e:
        print("Google fucked up")
    return text


def beep(what: int = 0):
    res = format(what, 'b')
    _str = ''
    for i in res:
        if i == '0':
            _str += 'dong '
        else:
            _str += 'ding '
    speak(_str)


def _test():
    speak("Привет, пользователь, это Dorrin, я приветствую тебя!")
    speak("Hello, user, it is Dorrin, да здравствует ИИ")


if __name__ == "__main__":
    _test()
