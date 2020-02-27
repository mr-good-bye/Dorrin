import pyttsx3
import speech_recognition as sr



def speak(text):
    engine = pyttsx3.init()
    engine.setProperty('voice', 'ru')
    engine.say(text)
    engine.runAndWait()
    del engine


def recognise():
    r = sr.Recognizer()
    mic = sr.Microphone()
    text = ''
    print("Listening")
    with mic as source:
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio, language = "ru-RU").lower()
    except sr.UnknownValueError:
        print("Невозможно расползнать голос")
    except sr.RequestError as e:
        print("Google fucked up")
    return text


def Beep(what = ''):
    pass  # TODO Beep


