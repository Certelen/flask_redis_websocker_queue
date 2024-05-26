from flask import Flask
from flask_sock import Sock
from huey import PriorityRedisHuey


DEBUG = True
SECRET_KEY = 'shhh, secret'

app = Flask(__name__)
app.config.from_object(__name__)
sock = Sock(app)

huey = PriorityRedisHuey()
