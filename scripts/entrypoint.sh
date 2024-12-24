#!/bin/bash
python manage.py collectstatic --settings=mysite.settings --noinput
python manage.py migrate --noinput
uwsgi --http "0.0.0.0:80" --module jura7park.wsgi:application --master --processes 4 --threads 2 --static-map /static=/code/staticfiles
