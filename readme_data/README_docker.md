## Запуск проекта в режиме демонстрации

1. **Клонирование репозитория:**
   - Клонируйте проект с помощью следующей команды:
     ```bash
     git clone git@github.com:lagodmi/Hackathon-HRSpace-x.git
     ```

2. **Переименование файла:**
   - Переименуйте файл `.env.example` в `.env`.

3. **Запуск проекта:**
   - Для запуска проекта в режиме демонстрации выполните следующие команды:
     ```bash
     docker compose -f docker-compose.yml up
     docker exec -it backend_HRSpace sh -c "python manage.py migrate && python manage.py loaddb && python manage.py collectstatic && cp -r /app/collected_static/. /backend_static/static/"
     ```

### Endpoint для доступа:

- POST: [http://127.0.0.1:8000/api/v1/inquiries/](http://127.0.0.1:8000/api/v1/inquiries/)
- GET: [http://127.0.0.1:8000/api/v1/inquiries/](http://127.0.0.1:8000/api/v1/inquiries/)
- GET по id заявки: [http://127.0.0.1:8000/api/v1/inquiries/id/](http://127.0.0.1:8000/api/v1/inquiries/id/)

**Ожидаемый JSON:** [expected_json.json](expected%20_json.json)