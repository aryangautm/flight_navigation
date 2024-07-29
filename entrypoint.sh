#!/bin/sh

# Run database migrations
python manage.py makemigrations
python manage.py migrate --no-input

# Collect static files (optional)
# python manage.py collectstatic --noinput

# Start the Django development server
exec "$@"
