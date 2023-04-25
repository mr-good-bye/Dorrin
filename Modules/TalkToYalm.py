"""
TaltToYalm module for Dorrin
version: 0.1
author: Nikita Trubitsyn
date: 2023-04-25
"""
import ssl

from requests import Session
from requests.adapters import HTTPAdapter
from urllib3.poolmanager import PoolManager

import Modules
from Configuration import Config

history = ''
c = Config('Modules/conf/tty.xml')


class AIAdapter(HTTPAdapter):
    def init_poolmanager(self, connections, maxsize, block=False, **kwargs):
        self.poolmanager = PoolManager(num_pools=connections,
                                       maxsize=maxsize,
                                       block=block,
                                       ssl_version=ssl.PROTOCOL_TLSv1,
                                       **kwargs)


@Modules.reg_module('')
def talk(prompt):
    global history, c
    _tmp = history.split()

    # Request to yalm
    s = Session()
    s.mount('https://', AIAdapter())
    history += f'\n{prompt}'
    prompt = f'вопрос: {prompt}\nкороткий ответ:'
    resp = s.post('https://zeapi.yandex.net/lab/api/yalm/text3', json={'query': prompt,
                                                                       'intro': 0, 'filter': 0})
    if resp.status_code != 200:
        return f"Что-то пошло не так. Балабоба вернул код {resp.status_code}"
    # Get the text or first line
    res = resp.json()['text']
    if c.get('talkative') == 'no':
        res = res[:res.find('\n')]
    history += f'\n{res}'

    # Make history to 25 lines
    if len(_tmp) > 25:
        history = '\n'.join(_tmp[-25:])
    return res


@Modules.reg_module('покажи историю')
def show_history(_):
    global history
    return history
