import ssl

from requests import Session
from requests.adapters import HTTPAdapter
from urllib3.poolmanager import PoolManager


class MyAdapter(HTTPAdapter):
    def init_poolmanager(self, connections, maxsize, block=False):
        self.poolmanager = PoolManager(num_pools=connections,
                                       maxsize=maxsize,
                                       block=block,
                                       ssl_version=ssl.PROTOCOL_TLSv1)


s = Session()
s.mount("https://", MyAdapter())


def exoooy(text):
    headers = {'Content-Type': 'application/json'}
    json = {"query": text, "intro": 0, "filter": 1}
    return s.post('https://zeapi.yandex.net/lab/api/yalm/text3',
                  json=json, headers=headers).json()


print(exoooy('Привет HABR'))
