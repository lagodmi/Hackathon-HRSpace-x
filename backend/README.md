- создать вирт окружение и установить зависимости

- переименовать файл .env.example в .env

- запустить docker-compose.postgresql.yml
    docker compose -f docker-compose.postgresql.yml up

- создать миграции
    python manage.py migrate

- зайти в контейнер
    docker container exec -it cf43fc78a981 psql -U user -d HRSpace_db
    - проверить появились ли таблицы стандартного набора
        \dt

- запустить проект на локалке и проверить что все без ошибок
    python manage.py runserver