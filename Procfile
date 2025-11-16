release: python manage.py migrate --noinput && python manage.py collectstatic --noinput && python manage.py populate_data --noinput
web: gunicorn fqcproj.wsgi --log-file -
