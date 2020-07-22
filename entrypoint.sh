python manage.py migrate
python manage.py collectstatic --no-input
gunicorn delve.wsgi:application --bind 0.0.0.0:$1
