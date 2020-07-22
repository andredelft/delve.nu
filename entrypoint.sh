python manage.py migrate
python manage.py collectstatic --noinput
gunicorn delve.wsgi:application --bind 0.0.0.0:$1
