#!/bin/bash

# Collect static files
echo "Collecting static files"
python manage.py collectstatic --settings=jura7park.settings --noinput

# Apply database migrations
echo "Applying database migrations"
python manage.py migrate --noinput

# Start the Django application using uWSGI as a non-root user
uwsgi --http "0.0.0.0:80" \
      --module jura7park.wsgi:application \
      --master \
      --processes 4 \
      --threads 2 \
      --static-map /static=/app/staticfiles \
      --uid appuser \
      --gid appgroup
