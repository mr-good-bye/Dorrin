from appJar import gui
from collections import deque
import SpeechWork
import Account_Manager
from os import _exit
# _______________________________________________PUBLIC VARS
modules = dict()

class BufferQueue:  # Класс для обмена данными между потоками в виде очереди
    b = deque()

    def set(self, data):
        self.b.append(data)
        print(data)
        return 1

    def get(self):
        try:
            return self.b.popleft()
        except IndexError:
            return 0


'''
c = ctime()

def count(set):
    while True:
        a= time.asctime()
        set(a)
        time.sleep(1)
        print("Thread")

timethr = Thread(target=count, args=(c.set,))
timethr.start()

app = gui()

app.addMessage(title = "time", text = c.get())

def update():
    app.setMessage(title = "time", text = c.get())
    print('updated with ' + c.get())

app.registerEvent(update)
#app.setStartFunction(timethr.start)
app.go()

print("But")
'''

SpeechWork.speak("Привет епты")
vkToken = Account_Manager.token
path = Account_Manager.path


try:
    import VkBotModule
except ModuleNotFoundError:
    print("Модуль ВК не подключен.")
else:
    modules['vk'] = True


if modules["vk"]:
    VkBot = VkBotModule.VkAccount("Name" + vkToken, path)



def speakHandler(event):
    for word in event:
        if str(word).lower() in ("ответь"):
            if str(event[event.index(word) + 1]).lower() in (""):  # TODO UserData + msgrs list
                if modules["vk"]:
                    i = event[event.index(word)]
                    name = event[i+1] + " " + event[i+2]
                    if name in VkBot.userData:
                        text = ''
                        for j in range(i+3, len(event)):
                            text = text + event[j] + ' '
                        VkBot.send(name, text)
                    else:
                        SpeechWork.speak("Пользователь не найден в базе")
        if str(word) in ("голос"):
            VkBot.isAloud("101010")
        if str(word) in ("закройся", "отключись"):
            _exit(0)
