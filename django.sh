#!/bin/bash
echo "Creating Migrations..."
python3 manage.py makemigrations djangoapp
echo ====================================

echo "Starting Migrations..."
python3 manage.py migrate
echo ====================================