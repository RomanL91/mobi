#!/usr/bin/env sh

# python manage.py makemigrations
# python manage.py migrate

python manage.py collectstatic
# python -m celery --app core worker -l info &

# gunicorn --bind 0.0.0.0:8000 core.asgi -w 4 -k uvicorn.workers.UvicornWorker
uvicorn core.asgi:application --host 0.0.0.0 --port 8000