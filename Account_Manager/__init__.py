"""Самостоятельный модуль!
1. Проверка наличия директории с файлами
2. Проверка наличия системных файлов
3. Графический интерфейс для входа в аккаунт"""


from appJar import gui
#Массив функций
foos = list()
path = ''
login, password = '', ''
files = list()
files.append('userList.doda')


mGui = gui()


def pathCheck():
    global path
    try:
        file = open('config.cfg', 'r')
        path = file.read()
        file.close()
    except FileNotFoundError:
        path = mGui.directoryBox(title="Config Directory", dirName=r'%AppData%')
        file = open('config.cfg', 'w+')
        file.write(path)
        file.close()
foos.append(pathCheck)


def fileCheck():
    for p1 in files:
        filepath = path + "\\" + p1
        try:
            file = open(filepath, 'r')
            file.close()
        except FileNotFoundError:
            file = open(filepath, 'w+')
            file.close()
foos.append(fileCheck)



def accLogin():
    mGui.startSubWindow("Vk Login")
    mGui.addEntry("login")
    mGui.addSecretEntry('password')
    def saveLog():
        global login
        global password
        login = mGui.getEntry('login')
        password = mGui.getEntry('password')
        mGui.destroySubWindow('Vk Login')
    mGui.addButton('Enter', saveLog)
    mGui.stopSubWindow()
    mGui.showSubWindow('Vk Login')
