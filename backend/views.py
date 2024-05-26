from flask import render_template
from flask_socketio import emit

from app import app, socketio
from tasks import user_task_1


@app.route('/')
def index():
    return render_template('index.html')


@socketio.on('test event')
def test_connect():
    message = user_task_1(2)
    emit('after connect', {'message': 'Задача в очереди'})
    emit('after connect', {'message': message(blocking=True)})
