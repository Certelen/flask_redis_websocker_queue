from flask import Flask, render_template
from flask_sock import Sock
from huey import PriorityRedisHuey
from huey.signals import SIGNAL_EXECUTING
import time
import redis

r = redis.Redis()
app = Flask(__name__)
sock = Sock(app)
huey = PriorityRedisHuey()

import tasks


@huey.signal(SIGNAL_EXECUTING)
def on_task_executing(signal, task):
    r.mset({'now_task': task.id + '|' + task.name})
    print(r.get('now_task'))


def deserialize_task(data):
    return huey.serializer.deserialize(data)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/admin')
def task_monitor():
    queue = [deserialize_task(task) for task in huey.storage.enqueued_items()]
    now = r.get('now_task').decode('utf-8').split('|')
    return render_template('task_monitor.html', queue=queue, now=now)


@sock.route('/test_route')
def test_connect(ws):
    while True:
        data = ws.receive()
        if data in ['Задача 1', 'Задача 2']:
            message = tasks.user_task_1()
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
    queue = [deserialize_task(task) for task in huey.storage.enqueued_items()]
    while True:
        new_queue = [deserialize_task(task)
                     for task in huey.storage.enqueued_items()]
        if queue != new_queue:
            queue = new_queue
            now = r.get('now_task').decode('utf-8').split('|')
            ws.send(render_template('queue_table.html', queue=queue, now=now))
        time.sleep(1)


if __name__ == '__main__':
    app.run(debug=True)
