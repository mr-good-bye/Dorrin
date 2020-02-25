'''
VkManager.login вызовет VkManager.lo и VkManager.passw
Доступными что бы их "просить"
'''

from appJar import gui

mGui = gui()
lo = ''
passw = ''
path1 = ''


def submit(login = "", password = ""):
    global lo
    global passw
    if not (login and password):
        login = mGui.getEntry("login")
        password = mGui.getEntry("password")
    else:
        mGui.destroyAllSubWindows()
    print(login, password)
    mGui.destroyAllSubWindows()
    lo = login
    passw = password
    file = open(path1, 'r')
    if file.read() == '':
        file.close()
        file = open(path1, 'w')
        file.write(lo+';'+passw)
        file.close()


def login(path):
    global path1
    path1 = path
    file = open(path, 'a')
    file.close()
    file = open(path, 'r')
    data = file.read()
    if data != '':
        login = data.split(';')
        submit(login[0], login[1])
        return 0
    mGui.startSubWindow("Vk Login")
    mGui.startLabelFrame("Account Details")
    mGui.setSticky("ew")
    mGui.addLabel("l1", "Login", 0, 0)
    mGui.addEntry("login", 0, 1)
    mGui.addLabel("l2", "Password", 1, 0)
    mGui.addSecretEntry("password", 1, 1)
    mGui.addButton("Login", submit, 2, 2, 0)
    mGui.stopLabelFrame()
    mGui.stopSubWindow()
    mGui.go(startWindow="Vk Login")


print("End Of Manager")