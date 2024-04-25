#!/bin/sh

# Exit script in case of error
set -e

# Run migrations
python manage.py makemigrations
python manage.py migrate

# Command to run Django with dynamic IP
python manage.py runserver 0.0.0.0:8000