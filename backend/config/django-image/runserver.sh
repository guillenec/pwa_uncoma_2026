#!/bin/bash

if [ ! -f manage.py ]; then
    django-admin startproject app .
fi

python manage.py makemigrations --noinput
python manage.py migrate --noinput

if [ -n "${DJANGO_SUPERUSER_USERNAME:-}" ]; then
    python manage.py shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.filter(username='${DJANGO_SUPERUSER_USERNAME}').exists() or User.objects.create_superuser(username='${DJANGO_SUPERUSER_USERNAME}', password='${DJANGO_SUPERUSER_PASSWORD}', email='${DJANGO_SUPERUSER_EMAIL}')"
fi

python manage.py runserver 0.0.0.0:8000

