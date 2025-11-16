release: python manage.py migrate --noinput && python manage.py collectstatic --noinput && python manage.py populate_data && python manage.py create_superuser
web: gunicorn fqcproj.wsgi --log-file -
