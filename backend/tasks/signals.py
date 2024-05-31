from huey.signals import SIGNAL_EXECUTING, SIGNAL_COMPLETE

from ..app import huey, r


"""Файл с обработкой сигналов от Huey"""


@huey.signal(SIGNAL_EXECUTING, SIGNAL_COMPLETE)
def on_task_status(signal, task):
    """
    При начале задачи - обновляем ключ текущей задачи в Редисе
    При выполнении задачи - опустошаем ключ текущей задачи в Редисе
    """
    if signal == 'executing':
        r.mset({'now_task': task.id + '|' + task.name})
    elif signal == 'complete':
        r.mset({'now_task': ''})
