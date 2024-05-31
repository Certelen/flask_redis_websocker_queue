from flask import Flask
from flask_sock import Sock
from huey import PriorityRedisHuey
import redis

r = redis.Redis()
app = Flask(__name__)
sock = Sock(app)
huey = PriorityRedisHuey()


"""
r - база данных Редиса
app - приложение Фласка
sock - Вебсокеты
huey - очередь задач Huey
"""
