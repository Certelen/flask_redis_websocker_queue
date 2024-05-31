from backend.app import app, huey  # noqa
import backend.tasks.tasks  # noqa
import backend.views  # noqa
import backend.websockets  # noqa
import backend.tasks.signals  # noqa

if __name__ == '__main__':
    """Главный файл запуска flask и huey"""
    app.run()
