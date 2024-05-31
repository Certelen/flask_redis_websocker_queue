from flask import render_template

from .app import app, r, huey
from .tasks import deserialize_task

"""Файл с обработчиками адресов"""


@app.route('/')
def index():
    """Главная"""
    return render_template('index.html')


@app.route('/admin')
def task_monitor():
    """Монитор очереди задач"""
    queue = [deserialize_task(task) for task in huey.storage.enqueued_items()]
    now = r.get('now_task').decode('utf-8')
    if now:
        now = now.split('|')
    return render_template('task_monitor.html', queue=queue, now=now)
