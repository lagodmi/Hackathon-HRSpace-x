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

### Ожидаемый json.

{
    "name": "название",
    "prof": {
        "id": 26,
        "prof_area": "Розничная торговля",
        "prof_name": "Директор магазина"
    },
    "city": {
        "id": "7439",
        "name": "Эрзин"
    },
    "salaryRange": {
        "salary_min": 40000,
        "salary_max": 50000
    },
    "employeeResponsibilities": [
        {"name": "Управление брендом компании"},
        {"name": "PR-деятельность и связи с общественностью"},
        {"name": "Анализ эффективности маркетинговых мероприятий"}
    ],
    "education": "Любое",
    "experience": 1,
    "citizenship": "Не имеет значения",
    "softwareSkills": [
        {"name": "Adobe Illustrator"},
        {"name": "Adobe InDesign"},
        {"name": "Google Docs"}
    ],
    "drivingLicense": false,
    "carOwnership": false,
    "workSchedule": "Вахтовый метод",
    "workFormat": "Полный день",
    "contractType": "Договор ГПХ с физ.лицом",
    "socialPackage": [
            {"name": "Гибкое начало дня"},
            {"name": "ДМС"},
            {"name": "ДМС со стоматологией"}
        ],
    "employeeReward": 10000000,
    "paymentType": "50% за выход + 50% по окончании гарантийного периода (1-3 мес.)",
    "employeeCount": 5,
    "recruiterTasks": [
        {"name": "Организация собеседований с заказчиком, синхронизация по времени соискателя и заказчика"},
        {"name": "Запрос рекомендаций с предыдущих мест работы"}
    ],
    "resumeFormat": "Резюме кандидатов, с которыми проведено интервью (с комментариями)",
    "dates": {
        "desiredFirstResumeDate": "2024-03-26",
        "desiredEmployeeExitDate": "2024-03-28"
    },
    "experienceYears": 4,
    "specialSkills": [
        {"name": "Проведение собеседований"},
        {"name": "Работа с HR-платформами"},
        {"name": "Оценка компетенций"}
    ],
    "additionalTasks": [
        {"name": "Организация тренингов и семинаров для повышения квалификации персонала"},
        {"name": "Ведение отчетности по итогам подбора персонала"},
        {"name": "Анализ эффективности каналов поиска кандидатов"}
    ],
    "isIndividual": true,
    "blacklistedCompanies": [
        {"name": "1C"}
    ],
    "recruiterCount": 1,
    "acceptOffer": true
}
