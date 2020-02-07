import SpeechWork
from vk_api.longpoll import VkLongPoll, VkEventType
import vk_api as vk
import sys
from threading import Thread as dick


class VkAccount:
    """Список аттрибутов и методов:
    name, token, vk_session, session_api, longpoll
    userData, vipData, aloud"""
    def userDataLoad(self):
        pass


    def __init__(self, uLogin, uPassword, filepath):
        self.vk_session = vk.VkApi(login=uLogin, password=uPassword, app_id=7297828,
                                   scope="friend, messages")
        self.vk_session.auth()
        self.vk_session._api_login()  # api True token
        self.session_api = self.vk_session.get_api()
        self.longpoll = VkLongPoll(self.vk_session)
        self.userData = dict()
        self.vipData = list()
        self.path = filepath
        self.userDataLoad()
        self.aloud = True


    def isAloud(self, boo = "101010"):
        if boo == "101010":
            self.aloud = not self.aloud
        else:
            self.aloud = boo


    def userDataSave(self):
        with open(self.path + r"\userData", 'w') as f:
            for name in self.userData:
                f.write(name)
                f.write(":")
                f.write(str(self.userData[name]))
                f.write(';')


    def userDataLoad(self):
        with open(self.path + r"\userData", 'r') as f:
            for line in f:
                data1 = ''
                sedData = list()
                for char in line:
                    if char not in ';:':
                        data1 = data1 + char
                    if char in ';:':
                        sedData.append(data1)
                        data1 = ''
                self.userData[sedData[0]] = sedData[1]


    def listenChat(self):
        while 'sense is LOST':
            for event in self.longpoll.listen():
                if event.type == VkEventType.MESSAGE_NEW and not event.from_me:
                    user = self.vk_session.method('users.get', {'user_ids': event.user_id})
                    name = str(user[0]['first_name']).capitalize() + ' ' + str(user[0]['last_name']).capitalize()
                    response = name + ': ' + event.text.lower()
                    if name not in self.userData:
                        self.userData[name] = event.user_id
                        self.userDataSave()
                    response = response.translate(dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd))
                    if self.aloud:
                        SpeechWork.speak(response)
                    else:
                        SpeechWork.beep('msg')
                if event.from_me and event.text.lower() == 'bot off':
                    break

    def send(self, name, text):
        name = name.lower()
        if name in self.userData:
            self.vk_session.method('messages.send', {'user_id': self.userData[name], 'message': text, 'random_id': 0})
            SpeechWork.speak("Сообщение отправлено!")
        else:
            SpeechWork.speak("Пользователь " + name + " не найден")
