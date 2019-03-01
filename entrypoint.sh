#!/usr/bin/env bash
set -e

celery -A ogamebot worker -l info -B >> celery.log 2>&1 &

echo 'yes' | python manage.py collectstatic --clear
gunicorn -c gunicorn_config.py ogamebot.wsgi >> gunicorn.log 2>&1 &

cp -r static/ /usr/share/nginx/html
cp -r nginx.conf /etc/nginx/conf.d/default.conf
nginx -g 'daemon off;'
