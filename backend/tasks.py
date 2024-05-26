import time

from huey import crontab

from app import huey


@huey.periodic_task(crontab(minute='*/1'))
def periodic_task_1():
    print('Начата периодическая задача 1')
    time.sleep(10)
    print('Закончена периодическая задача 1')


@huey.periodic_task(crontab(minute='*/1'))
def periodic_task_2():
    print('Начата периодическая задача 2')
    time.sleep(10)
    print('Закончена периодическая задача 2')


@huey.periodic_task(crontab(minute='*/1'))
def periodic_task_3():
    print('Начата периодическая задача 3')
    time.sleep(10)
    print('Закончена периодическая задача 3')


@huey.periodic_task(crontab(minute='*/1'))
def periodic_task_4():
    print('Начата периодическая задача 4')
    time.sleep(10)
    print('Закончена периодическая задача 4')


@huey.periodic_task(crontab(minute='*/1'))
def periodic_task_5():
    print('Начата периодическая задача 5')
    time.sleep(10)
    print('Закончена периодическая задача 5')


@huey.periodic_task(crontab(minute='*/1'))
def periodic_task_6():
    print('Начата периодическая задача 6')
    time.sleep(10)
    print('Закончена периодическая задача 6')


@huey.task(priority=10)
def user_task_1(n):
    print('Закончена пользовательская задача 1')
    time.sleep(5)
    print('Закончена пользовательская задача 1')
    return 'Задача выполнена'
