переименовать файл:

.env.example -> .env

КОНСОЛЬ!!! находясь в корневой директории:

- docker compose -f docker-compose.yml up
- docker exec -it backend_HRSpace sh -c "python manage.py migrate && python manage.py loaddb && python manage.py collectstatic && cp -r /app/collected_static/. /backend_static/static/"
  
backend развернут и доступен по endpoint:

POST

- http://127.0.0.1:8000/api/v1/inquiries/

GET

- http://127.0.0.1:8000/api/v1/inquiries/

GET id-заявки

- http://127.0.0.1:8000/api/v1/inquiries/id/
