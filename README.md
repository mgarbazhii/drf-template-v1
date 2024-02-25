# drf-template-v1

# Создаем виртуальное окружение

    python3 -m venv env

# Активируем окружение

    source env/bin/activate

# Обновляем менеджер пакетов

    pip install --upgrade pip

# Или устанавливаем все из файла requirements.txt

    pip install -r requirements.txt

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

