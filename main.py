"""
@author = Lanity_Roshoose
created 25.02.2020
"""
import VkBot
import VkBot.VkManager as VkManager
import SpeechWork
from threading import Thread as dick
from appJar import gui
from _collections import deque
import time


mGui = VkManager.mGui  # Определение ГУИ
cfgPath = ''


# Класс для обмена данными между потоками и ГУИ используя основной поток
class BufferQueue:
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


buf = BufferQueue()


# Проверка и создание конфига с директорией системных файлов
def _start_():
    conf = open("conf.cfg", 'a')
    conf.close()
    conf = open("conf.cfg", 'r')
    path = conf.read()
    conf.close()
    if path == '':
        path = mGui.directoryBox(title="Choose cfg directory", dirName=r'%AppData%')
        conf = open("conf.cfg", 'w')
        conf.write(path)
        conf.close()
    global cfgPath
    cfgPath = path


_start_()
VkManager.login(cfgPath+r'/acc.cfg')
bot = VkBot.VkAccount(VkManager.lo, VkManager.passw, cfgPath)
listening = dick(target=bot.listenChat, args=(buf.set,))
listening.start()


# TODO main GUI
class GUI:
    def execute(self, btn):
        handler(self.mGui.getEntry("message").split(' '))
        self.mGui.setEntry("message", "")

    def update(self):
        pass

    def __init__(self, buffer, gui):
        self.mGui = gui
        self.buffer = buffer
        self.text = ""
        self.mGui.startSubWindow("VkBot")
        self.mGui.setSize("800x600")
        #self.mGui.startLabelFrame("VkGui")
        self.mGui.addEmptyMessage("LastMsg")
        self.mGui.addEntry("message")
        self.mGui.addButton("Exec", self.execute)
        #self.mGui.stopLabelFrame()
        self.mGui.stopSubWindow()

        thr = dick(target=self.update, args = (self.buffer,))
        thr.start()
        self.mGui.go(startWindow="VkBot")

    def update(self, get):
        while True:
            bf = get()
            print(bf)
            if bf != 0:
                self.text = self.text + '\n' + bf
                print(self.text)
                self.mGui.clearMessage("LastMsg")
                self.mGui.setMessage("LastMsg", self.text)
            time.sleep(0.5)


def handler(event):
    print(event)
    for word in event:
        if str(word).lower() in ('ответь'):
            i = event.index(word)
            name = event[i+1] + " " + event[i+2]
            if name in bot.userData:
                text = ''
                for j in range(i+3, len(event)):
                    text = text + event[j] + ' '
                bot.send(name, text)
            else:
                SpeechWork.speak("Пользователь не найден")
            break


def spThr():
    while 'nothing':
        handler(SpeechWork.recognise())



dgui = GUI(buf.get, mGui)


tSpThr = dick(target = spThr)
#tSpThr.start()