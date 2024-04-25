#!/bin/sh

# Exit script in case of error
set -e

# Run migrations
echo "Creating Migrations..."
python manage.py makemigrations
echo ====================================

echo "Starting Migrations..."
python manage.py migrate
echo ====================================

echo "Starting server"
python manage.py runserver 0.0.0.0:8000
echo ====================================