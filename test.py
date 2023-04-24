import Modules as m
import SpeechWork as sw





def speech_test():
    a = ''
    while a != 'выход':
        a = sw.recognise()
        print(sw.speak(m.handler(a)))


if __name__ == "__main__":
    #speech_test()
    sw.speak(m.handler('сколько времени'))
