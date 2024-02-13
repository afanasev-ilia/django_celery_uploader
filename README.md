# django_celery_uploader

## Описание
Django приложение которое позволяет загружать файлы на сервер, а затем асинхронно обрабатывать их с использованием Celery.

## Технологии

Python 3.9.10
Django 3.2
Django REST framework 3.14

## Запуск проекта локально

Клонируем репозиторий и переходим в него в командной строке:
```bash
git clone git@github.com:afanasev-ilia/django_celery_uploader.git
```
```bash
cd django_celery_uploader
```

Запускаем docker-compose:
```bash
docker-compose up -d --build
```

Выполняем миграции:
```bash
docker-compose exec django_celery_uploader python manage.py migrate
```

Создаем суперппользователя:
```bash
docker-compose exec django_celery_uploader python manage.py createsuperuser
```

Останавливаем собранные контейнеры:
```bash
docker-compose down -v 
```

## Шаблон наполнения .env
```
SECRET_KEY='********************************'
```

## Автор
Илья Афанасьев
