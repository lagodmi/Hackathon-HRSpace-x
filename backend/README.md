## Запуск проекта

1. **Клонирование репозитория:**
   - Клонируйте проект с помощью следующей команды:
     ```bash
     git clone git@github.com:lagodmi/Hackathon-HRSpace-x.git
     ```

2. **Переименование файла:**
   - Переименуйте файл `.env.example` в `.env`.

3. **Запуск PostgreSQL:**
   - Для запуска PostgreSQL используйте docker-compose:
     ```bash
     docker compose -f docker-compose.postgresql.yml up
     ```

4. **Настройка базы данных в файле settings:**
   - Для настройки базы данных в файле settings, ознакомьтесь с возможными настройками DATABASE в [этом файле](readme_data/setting_DATABASES).

5. **Выполнение команды для запуска проекта:**
   - Выполните следующую команду для миграции базы данных, загрузки данных и запуска сервера:
     ```bash
     python manage.py migrate && python manage.py loaddb && python manage.py runserver
     ```

### Endpoint для доступа к backend:

- POST: [http://127.0.0.1:8000/api/v1/inquiries/](http://127.0.0.1:8000/api/v1/inquiries/)
- GET: [http://127.0.0.1:8000/api/v1/inquiries/](http://127.0.0.1:8000/api/v1/inquiries/)
- GET по id заявки: [http://127.0.0.1:8000/api/v1/inquiries/id/](http://127.0.0.1:8000/api/v1/inquiries/id/)

**Ожидаемый JSON:** [expected_json.json](backend/readme_data/expected%20_json.json)
