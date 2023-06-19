#!/bin/bash

docker exec loan-management-server python manage.py migrate
docker exec \
	-e "DJANGO_SUPERUSER_USERNAME=admin" \
	-e "DJANGO_SUPERUSER_PASSWORD=admin" \
	-e "DJANGO_SUPERUSER_EMAIL=admin@admin.com" \
	loan-management-server python manage.py createsuperuser --no-input