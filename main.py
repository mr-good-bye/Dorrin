"""
@author = Lanity_Roshoose
created 25.02.2020
"""
import VkBot
import VkBot.VkManager as VkManager
import SpeechWork
from threading import Thread as dick
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
        self.mGui.setSize("800x350")
        #self.mGui.startLabelFrame("VkGui")
        self.mGui.startScrollPane(title="pane", row=0, column=0,rowspan=10,  sticky="new")
        self.mGui.setScrollPaneWidth("pane",800)
        self.mGui.addEmptyMessage("LastMsg")
        self.mGui.setMessageWidth("LastMsg", 750)
        self.mGui.stopScrollPane()
        self.mGui.addEntry("message", 10)
        self.mGui.setEntryWidth("message", 800)
        self.mGui.addButton("Exec", self.execute, 11)
        #self.mGui.stopLabelFrame()
        self.mGui.setLocation(x=200,y=100)
        self.mGui.show()
        self.mGui.stopSubWindow()

        thr = dick(target=self.update, args = (self.buffer,))
        thr.start()
        self.mGui.go(startWindow="VkBot")

    """def update(self, get):
        spis = list()
        for i in range(5):
            spis.append(i + '.')
        while True:
            bf = get()
            print(bf)
            if bf != 0:
                for i in range(4):
                    list[i] = list[i+1]
                list[5] = bf
                self.text = ''
                for i in range(5):
                    self.text = self.text + spis[i] + "\n"
                print(self.text)
                self.mGui.clearMessage("LastMsg")
                self.mGui.setMessage("LastMsg", self.text)
            time.sleep(0.5)"""
    def update(self, get):
        while True:
            bf = get()
            if bf != 0:
                self.text = self.mGui.getMessage("LastMsg")
                self.mGui.setMessage("LastMsg", bf + "\n" + self.text)
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
        if str(word).lower() in ('1'):
            buf.set('Test =)')


def spThr():
    while 'nothing':
        handler(SpeechWork.recognise())


print("he")
tSpThr = dick(target = spThr)
tSpThr.start()

dgui = GUI(buf.get, mGui)
print("Hello")


