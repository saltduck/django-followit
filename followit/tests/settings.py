import os

DIRNAME = os.path.dirname(__file__)
DATABASE_ENGINE = 'sqlite3'
DATABASE_NAME = os.path.join(DIRNAME, 'database.db')

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'followit',
    'followit.tests'
)

SECRET_KEY = '1234567890'
