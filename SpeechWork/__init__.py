"""Модуль для работы с голосом."""

import pyttsx3  # TTS
import speech_recognition as sr
import pyaudio


def speak(text):
    """Функция создает движок, воспроизводит текст и удаляет движок"""
    engine = pyttsx3.init()
    engine.setProperty('voice', 'ru')
    engine.say(text)
    engine.runAndWait()
    del engine


def recognise():
    """Функция, возвращающая текст"""
    r = sr.Recognizer()
    mic = sr.Microphone()
    with mic as source:
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio, language = "ru-RU").lower()
    except sr.UnknownValueError:
        print("Невозможно распознать голос")
    except sr.RequestError as e:
        print("Google сказал, что все плохо: {0}".format(e))
    return text


def beep(event):
    pass  # TODO Реализация сигнала
