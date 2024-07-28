#!/bin/bash

# Wait for the database to be ready
echo "Waiting for postgres..."
while ! nc -z db 5432; do
  sleep 1
done
echo "PostgreSQL started"

# Run database migrations
python manage.py makemigrations
python manage.py migrate

# Collect static files (optional)
# python manage.py collectstatic --noinput

# Start the Django development server
exec "$@"
