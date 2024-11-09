#!/usr/bin/env bash

# collect static files
python manage.py collectstatic --noinput

# migrations
python manage.py migrate

# run server
python manage.py runserver 0:80

# run server with debug
# python -m debugpy --listen 0.0.0.0:5678 manage.py runserver 0.0.0.0:80
