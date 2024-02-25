# drf-template-v1

# Создаем виртуальное окружение

    python3 -m venv env

# Активируем окружение

    source env/bin/activate

# Обновляем менеджер пакетов

    pip install --upgrade pip

# Устанавливаем Django

    pip install django

# Устанавливаем необходимые пакеты

    pip install djangorestframework django-filter django-environ django-cors-headers djoser drf-spectacular

# Устанавливаем вспомогательные пакеты для разработки и отладки

    pip install django-extensions

# Устанавливаем пакет для PostGresq

    pip install psycopg2-binary

# Сохраняем пакеты в requirements.txt

    pip freeze > requirements.txt

# Или устанавливаем все из файла requirements.txt

    pip install -r requirements.txt

# Создаем проект в текущей директории

    django-admin startproject config .

# Обновляем файл settings.py:

    INSTALLED_APPS += [
        'rest_framework',
        'django_filters',
        'corsheaders',
        'djoser',
    ]

    MIDDLEWARE += [
        'corsheaders.middleware.CorsMiddleware',
        'django.middleware.common.CommonMiddleware',
    ]

    # CORS HEADERS (вынести в .env)

    CORS_ORIGIN_ALLOW_ALL = True
    CORS_ALLOW_CREDENTIALS = True
    CORS_ALLOW_HEADERS = ['*']
    CSRF_COOKIE_SECURE = False

# Создаем файл .env и заполняем его (S_K переносим из файла settings.py):

    SECRET_KEY=''
    DJANGO_DEBUG=True
    ALLOWED_HOSTS='127.0.0.1 LOCALHOST localhost'
    PG_DATABASE='postgres'
    PG_USER='postgres'
    PG_PASSWORD='postgres'
    DB_HOST='localhost'
    DB_PORT=5432

# Запускаем БД PostGreSQL в docker

    docker run -itd -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=postgres -p 5432:5432 -v data:/var/lib/postgresql/data --name postgresql postgres

# Обновляем файл settings.py:

    import environ
    import os

    env = environ.Env()  # get environment variables from .env file
    root = environ.Path(__file__) - 2  # get root of the project
    environ.Env.read_env(env.str(root(), '.env'))  # reading .env file

    BASE_DIR = root()
    SECRET_KEY = env.str('SECRET_KEY')
    DEBUG = env.bool('DEBUG', default=False)
    ALLOWED_HOSTS = env.str('ALLOWED_HOSTS').split(' ')

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': env.str('PG_DATABASE', default='postgres'),
            'USER': env.str('PG_USER', default='postgres'),
            'PASSWORD': env.str('PG_PASSWORD', default='postgres'),
            'HOST': env.str('DB_HOST', default='localhost'),
            'PORT': env.str('DB_PORT', default='5432'),
        },
    }

    STATIC_URL = 'static/'
    STATIC_ROOT = os.path.join(BASE_DIR, 'static')
    MEDIA_URL = '/media/'
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

    # import pdb
    # pdb.set_trace()
