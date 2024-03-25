# НАЗВАНИЕ.
## Описание проекта:
- 
## Стек проекта:
- Python 3.9
- Django 3.2.3
- Django REST framework 3.12.4
- JavaScript
## Cсылка на развернутый проект:
- 
## Процесс запуска проекта (через docker compose):
### Какую версию развернуть:
- В случае развертывания проекта в производственной среде следует использовать docker-compose.production.yml.
- Для разработки, тестирования или демонстрации концепции docker-compose.yml.
### Запуск проекта:
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

[ожидаемый json](backend/expected%20_json.json)

### Пример запросов:
- 
## Автор проекта:
