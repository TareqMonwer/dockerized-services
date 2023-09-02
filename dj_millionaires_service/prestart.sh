#!/bin/bash

python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser --username=admin --email=admin@admin.com --noinput
python manage.py runserver 0.0.0.0:8000