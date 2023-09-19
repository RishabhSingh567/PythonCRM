python manage.py collecstatic --no-input

python manage.py migrate

gunicorn --worker-tmp-dir /dev/sh djcrm.wsgi