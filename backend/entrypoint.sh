#!/bin/sh

python manage.py migrate --no-input
python manage.py collectstatic --no-input

gunicorn -b :8080 --certfile /etc/ssl/cert.pem --keyfile /etc/ssl/cert.key backend.wsgi