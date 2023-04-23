import Modules
import datetime


def datetime_to_str(dt: datetime.datetime):
    months = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь',
              'ноябрь', 'декабрь']
    return f'{dt.day} {months[dt.month-1]} {dt.year} в {dt.hour}:{dt.minute}'


@Modules.reg_module(('сколько времени', 'what time'))
def time(res):
    return datetime_to_str(datetime.datetime.now())


@Modules.reg_module('')
def _any(res):
    return 'Я не понимаю что вы хотите'


@Modules.reg_module(('повтори', 'repeat'))
def echo(res):
    i = max(res.lower().find('повтори')+7, res.lower().find('repeat')+6)
    return res[i:].strip()


@Modules.reg_module('выход')
def _exit(res):
    return None

