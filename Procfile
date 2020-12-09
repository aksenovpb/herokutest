release: python manage.py migrate
web: gunicorn herokutest.wsgi --log-file -
worker: python manage.py run_huey