from huey import crontab
import time

from . import huey

"""Файл с задачами"""


@huey.periodic_task(crontab(minute='*/1'))
def periodic_task_1():
    """Периодическая задача, запускается каждую минуту"""
    print('Начата периодическая задача 1')
    time.sleep(9)
    print('Закончена периодическая задача 1')


@huey.periodic_task(crontab(minute='*/1'))
def periodic_task_2():
    """Периодическая задача, запускается каждую минуту"""
    print('Начата периодическая задача 2')
    time.sleep(9)
    print('Закончена периодическая задача 2')


@huey.periodic_task(crontab(minute='*/1'))
def periodic_task_3():
    """Периодическая задача, запускается каждую минуту"""
    print('Начата периодическая задача 3')
    time.sleep(9)
    print('Закончена периодическая задача 3')


@huey.periodic_task(crontab(minute='*/1'))
def periodic_task_4():
    """Периодическая задача, запускается каждую минуту"""
    print('Начата периодическая задача 4')
    time.sleep(9)
    print('Закончена периодическая задача 4')


@huey.periodic_task(crontab(minute='*/1'))
def periodic_task_5():
    """Периодическая задача, запускается каждую минуту"""
    print('Начата периодическая задача 5')
    time.sleep(9)
    print('Закончена периодическая задача 5')


@huey.periodic_task(crontab(minute='*/1'))
def periodic_task_6():
    """Периодическая задача, запускается каждую минуту"""
    print('Начата периодическая задача 6')
    time.sleep(9)
    print('Закончена периодическая задача 6')


@huey.task(priority=10)
def user_task_1():
    """Пользовательская задача, запускается пользователем"""
    print('Начата пользовательская задача 1')
    time.sleep(5)
    print('Закончена пользовательская задача 1')
    return 'Задача выполнена'
