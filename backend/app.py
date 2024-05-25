from flask import Flask
from flask_socketio import SocketIO
from huey import PriorityRedisHuey


DEBUG = True
SECRET_KEY = 'shhh, secret'

app = Flask(__name__)
app.config.from_object(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

huey = PriorityRedisHuey()
