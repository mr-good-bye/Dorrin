"""
Sample module for Dorrin
version: 0.6
author: Nikita Trubitsyn
date: 2023-04-24
"""

import datetime

import Modules


def datetime_to_str(dt: datetime.datetime):
    months = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь',
              'ноябрь', 'декабрь']
    return f'{dt.day} {months[dt.month - 1]} {dt.year} в {dt.hour}:{dt.minute}'


@Modules.reg_module(('сколько времени', 'what time'))
def time(_):
    return datetime_to_str(datetime.datetime.now())


# @Modules.reg_module('')
def _any(_):
    return 'Я не понимаю что вы хотите'


@Modules.reg_module(('повтори', 'repeat'))
def echo(prompt):
    i = max(prompt.lower().find('повтори') + 7, prompt.lower().find('repeat') + 6)
    return prompt[i:].strip()


@Modules.reg_module('выход')
def _exit(_):
    raise KeyboardInterrupt('End from prompt')
