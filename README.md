# Микросервис с вебсокетом и очередью задач
## Описание
Имеется 6 периодических задач по 10 секунд и 1 пользовательская задача на 5 секунд. После нажатия кнопки на клиенте пользовательская задача выполняется сразу после текущей периодической и возвращает ответ.
## Технологии
- Python 3.11
- Redis 5.0.4
- Flask 3.0.3
- Flask Sock 0.7.0
- Huey 2.5.0

# Установка
## Копирование репозитория
Клонируем репозиторий и переходим в папку проекта:
```
~ git@github.com:Certelen/flask_redis_websocker_queue.git
~ cd flask_redis_websocker_queue
```

## Развертывание на текущем устройстве:
# Подготовка
Перемещаем файлы настроек (gunicorn.service, huey.service) в папку /etc/systemd/system/
Запускаем службы:
```
systemctl enable gunicorn
systemctl start gunicorn
systemctl enable huey
systemctl start huey
```
Перемещаем файл настроек 000-default.conf в папку /etc/apache2/sites-enabled/
Активация домена, перенаправления веб-сокетов:
```
a2enmod proxy_http
a2ensite 000-default.conf
```
Запуск, перезапуск сервера:
```
systemctl start apache2
systemctl restart apache2
```

Устанавливаем и активируем виртуальное окружение из папки с проектом
```
~ py -3.11 -m venv venv
~ . venv/Scripts/activate
```
Устанавливаем требуемые зависимости:
```
~ pip install -r requirements.txt
```
# Запуск
В первом терминале запускаем Flask-сервер
```
~ ./run_webapp.sh
```
Во втором терминале запускаем Huey-очередь
```
~ ./run_huey.sh
```
# Адресные пути
- [Главная](http://127.0.0.1:5000/)