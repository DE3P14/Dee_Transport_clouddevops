#!/bin/bash
# eb_deploy.sh

# Activate virtual environment
source /var/app/venv/*/bin/activate

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput

# Start Gunicorn
echo "Starting Gunicorn..."
exec gunicorn -b :8000 --access-logfile - --error-logfile - busapp.wsgi:application
