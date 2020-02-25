#import VkManager
from vk_api.longpoll import VkLongPoll, VkEventType
import vk_api as vk
import sys
from threading import Thread as dick
import SpeechWork

class VkAccount:


    def userDataLoad(self):
        pass

    def __init__(self, uLo, uPassw, filepath):
        self.vk_session = vk.VkApi(login=uLo,
                                   password=uPassw,
                                   app_id=7297828,
                                   scope="friend, messages")
        self.vk_session.auth()
        self.vk_session._api_login()
        self.session_api = self.vk_session.get_api()
        self.longpoll = VkLongPoll(self.vk_session)
        self.userData = dict()
        self.path = filepath
        self.userDataLoad()
        self.aloud = True
        print("Vk defined!")


    def isAloud(self, boo = "101010"):
        if boo == "101010":
            self.aloud = not self.aloud
        else:
            self.aloud = boo


    def userDataSave(self):
        with open(self.path + r'\userData', 'w') as f:
            for name in self.userData:
                f.write(name+':'+str(self.userData[name])+'\n')


    def userDataLoad(self):
        f = open(self.path + r'\userData', 'a')
        f.close()
        with open(self.path + r'\userData', 'r') as f:
            for line in f:
                data = line.split(':')
                self.userData[data[0]] = data[1]


    def listenChat(self, set):
        while 'sense is LOST':
            for event in self.longpoll.listen():
                if event.type == VkEventType.MESSAGE_NEW or event.type == VkEventType.MESSAGE_EDIT:
                    #try:
                    user = self.vk_session.method('users.get', {'user_ids': event.user_id})
                    #except:
                        #continue
                    name = str(user[0]['first_name']).capitalize() + ' ' + str(user[0]['last_name']).capitalize()
                    response = name + ': ' + event.text
                    if name.lower() not in self.userData:
                        self.userData[name.lower()] = event.user_id
                        self.userDataSave()
                    response = response.translate(dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd))
                    set(response)
                    if self.aloud:
                        SpeechWork.speak(response)
                    else:
                        SpeechWork.beep('msg')
                    print(response)


    def send(self, name, text):
        name = name.lower()
        if name in self.userData:
            print(name, ' : ', text, '\n', self.userData[name])
            self.vk_session.method('messages.send', {'user_id': int(self.userData[name]), 'message': text, 'random_id':0})

