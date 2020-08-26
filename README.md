# Test task

## How to start?
Нужно ввести следующие команды:
```
- git clone https://github.com/sergiishevchenko/resizer-image.git
- python3 -m venv myenv && source myenv/bin/activate && pip install -r requirements.txt
- python manage.py makemigrations test_project
- python manage.py migrate
- python3 manage.py runserver

```
После запуска Django появится ссылка типа http://127.0.0.1:8000/ - нажмите на неё.

Приложение готово для локального использования!

## How to use Docker?

```
- docker build .  // создание образа
- docker-compose build   // создание docker образа
- docker-compose up -d  // обновление docker образа
- docker-compose logs -f  // логи
- docker ps -a   // просмотреть все активные контейнеры
```
