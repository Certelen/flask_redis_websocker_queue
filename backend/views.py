from flask import render_template

from app import app, sock
from tasks import user_task_1


@app.route('/')
def index():
    return render_template('index.html')


@sock.route('/test_route')
def test_connect(ws):
    while True:
        data = ws.receive()
        if data is not None:
            message = user_task_1(2)
            ws.send('Задача в очереди')
            ws.send(message(blocking=True))
