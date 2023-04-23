import Modules as m
import SpeechWork as sw


#print(sw.speak(m.handler('сколько времени?')))
#print(sw.speak(m.handler('Huesos')))
#print(sw.speak(m.handler('Повтори Я гей')))

a = ''
while a != 'выход':
    a = sw.recognise()
    print(sw.speak(m.handler(a)))
