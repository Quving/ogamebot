#!/usr/bin/env bash
set -e

celery -A ogamebot worker -l info -B >> celery.log 2>&1 &

echo 'yes' | python manage.py collectstatic --clear
gunicorn -c gunicorn_config.py sharelog.wsgi
