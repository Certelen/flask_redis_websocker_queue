import tasks
import views
from app import app, huey, socketio

if __name__ == '__main__':
    socketio.run(app, debug=True)
