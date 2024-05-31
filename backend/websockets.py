from flask import render_template
import time

from .app import sock, r, huey
from .tasks import deserialize_task
from .tasks.tasks import user_task_1


"""Файл с обработчиком входящих вебсокетов"""


@sock.route('/test_route')
def test_connect(ws):
    """
    Получение нажатия кнопки пользователем
    Проверка что нажата кнопка с задачей
    Постановка пользовательской задачи в очередь с приоритетом
    Вывод пользователю информации когда задача будет взята в работу
    ИЛИ если задача взята и выполнена менее чем за секунду - вывод результата
    """
    while True:
        data = ws.receive()
        if data in ['Задача 1', 'Задача 2']:
            message = user_task_1()
            ws.send('Задача в очереди')
            while message() is None:
                if (message.id ==
                        r.get('now_task').decode('utf-8').split('|')[0]):
                    ws.send('Задача в работе')
                    break
                time.sleep(1)
            ws.send(message(blocking=True))


@sock.route('/update_route')
def update_route(ws):
    """
    Обновление монитора очереди задач
    Проверяем изменения в очереди и текущей задаче каждую секунду
    При изменении - отправляем html-шаблон с новыми данными клиенту
    """
    queue = [deserialize_task(task) for task in huey.storage.enqueued_items()]
    now = r.get('now_task').decode('utf-8')
    while True:
        new_queue = [deserialize_task(task)
                     for task in huey.storage.enqueued_items()]
        new_now = r.get('now_task').decode('utf-8')
        if queue != new_queue or now != new_now:
            queue = new_queue
            now = new_now
            if now:
                now = now.split('|')
            ws.send(render_template('queue_table.html', queue=queue, now=now))
        time.sleep(1)
