from drf_spectacular.utils import extend_schema, OpenApiExample, OpenApiParameter
from rest_framework import permissions, serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import InquiryGetSerializer, InquirySerializer, DutySerializer


class DummyDetailStatusSerializer(serializers.Serializer):
    status = serializers.IntegerField()
    details = serializers.CharField()


inquiry_list_schema = extend_schema(
    summary="Получить список заявок",
    responses={
            status.HTTP_200_OK: InquiryGetSerializer,
            status.HTTP_400_BAD_REQUEST: DummyDetailStatusSerializer,
            status.HTTP_401_UNAUTHORIZED: DummyDetailStatusSerializer,
            status.HTTP_403_FORBIDDEN: DummyDetailStatusSerializer,
    },
    examples=[
                OpenApiExample(
                    "Get example",
                    description="Пример для get-запроса заявки",
                    value={
                        "name": "Автомойщик",
                        "prof": {
                            "id": 239,
                            "prof_area": "Автомобильный бизнес",
                            "prof_name": "Автомойщик"
                        },
                        "city": {
                            "id": 21,
                            "name": "Красноярск"
                        },
                        "salaryRange": {
                            "salary_min": 111111,
                            "salary_max": 222222
                        },
                        "employeeResponsibilities": [
                            "PR-деятельность и связи с общественностью",
                            "Активные продажи"
                        ],
                        "education": "Неоконченное высшее",
                        "experience": 3,
                        "citizenship": "РФ",
                        "softwareSkills": [
                            "Adobe Photoshop",
                            "Adobe Premiere Pro"
                        ],
                        "drivingLicense": True,
                        "carOwnership": False,
                        "workSchedule": "Вахтовый метод",
                        "workFormat": "Гибридный формат",
                        "contractType": "Договор ГПХ с физ.лицом",
                        "socialPackage": [
                            "Гибкое начало дня",
                            "ДМС"
                        ],
                        "employeeReward": 322322,
                        "paymentType": "100% за выход сотрудника",
                        "employeeCount": 3,
                        "recruiterTasks": [
                            "Запрос рекомендаций с предыдущих мест работы",
                            "Организация собеседований с заказчиком, синхронизация по времени соискателя и заказчика"
                        ],
                        "resumeFormat": "Резюме без предварительного собеседования",
                        "dates": {
                            "desiredFirstResumeDate": "23-03-2024",
                            "desiredEmployeeExitDate": "24-03-2024"
                        },
                        "experienceYears": 3,
                        "specialSkills": [
                            "Headhunting",
                            "Анализ рынка труда"
                        ],
                        "additionalTasks": [
                            "Анализ эффективности каналов поиска кандидатов",
                            "Мониторинг удовлетворенности сотрудников и разработка мероприятий по её повышению"
                        ],
                        "isIndividual": True,
                        "blacklistedCompanies": [
                            "AEON Corporation"
                        ],
                        "recruiterCount": 2
                        },
                    status_codes=[str(status.HTTP_200_OK)],
                ),
            ],
)

inquiry_update_schema = extend_schema(
    summary="Изменение существующей заявки",
    responses={
            status.HTTP_200_OK: InquirySerializer,
            status.HTTP_400_BAD_REQUEST: DummyDetailStatusSerializer,
            status.HTTP_401_UNAUTHORIZED: DummyDetailStatusSerializer,
            status.HTTP_403_FORBIDDEN: DummyDetailStatusSerializer,
    }
)

inquiry_create_schema = extend_schema(
    summary="Создание новой заявки",
    responses={
            status.HTTP_200_OK: InquirySerializer,
            status.HTTP_400_BAD_REQUEST: DummyDetailStatusSerializer,
            status.HTTP_401_UNAUTHORIZED: DummyDetailStatusSerializer,
            status.HTTP_403_FORBIDDEN: DummyDetailStatusSerializer,
    },
    examples=[
                OpenApiExample(
                    "Post example",
                    description="Пример для post-запроса заявки",
                    value={
                        "name": "Маша",
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
                        "drivingLicense": False,
                        "carOwnership": False,
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
                            "desiredFirstResumeDate": "26-03-2024",
                            "desiredEmployeeExitDate": "28-03-2024"
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
                        "isIndividual": True,
                        "blacklistedCompanies": [
                            {"name": "1C"}
                        ],
                        "recruiterCount": 1,
                        "acceptOffer": True
                    },
                    status_codes=[str(status.HTTP_200_OK)],
                ),
            ],
)

inquiry_retrieve_schema = extend_schema(
    summary="Детальная информация о заявке",
    responses={
            status.HTTP_200_OK: InquiryGetSerializer,
            status.HTTP_400_BAD_REQUEST: DummyDetailStatusSerializer,
            status.HTTP_401_UNAUTHORIZED: DummyDetailStatusSerializer,
            status.HTTP_403_FORBIDDEN: DummyDetailStatusSerializer,
    }
)

inquiry_delete_schema = extend_schema(
    summary="Удаление заявки",
    responses={
            status.HTTP_200_OK: InquiryGetSerializer,
            status.HTTP_400_BAD_REQUEST: DummyDetailStatusSerializer,
            status.HTTP_401_UNAUTHORIZED: DummyDetailStatusSerializer,
            status.HTTP_403_FORBIDDEN: DummyDetailStatusSerializer,
    }
)

duty_list_schema = extend_schema(
    summary="Список обязанностей",
    responses={
            status.HTTP_200_OK: DutySerializer,
            status.HTTP_400_BAD_REQUEST: DummyDetailStatusSerializer,
            status.HTTP_401_UNAUTHORIZED: DummyDetailStatusSerializer,
            status.HTTP_403_FORBIDDEN: DummyDetailStatusSerializer,
    },
    parameters=[
            OpenApiParameter(
                name='prof_area',
                location=OpenApiParameter.QUERY,
                description='Параметр для поиска навыков выбранной проф.области',
                required=False,
                type=str
            ),
    ],
    examples=[
                OpenApiExample(
                    "get duties list example",
                    description="Пример для get-запроса списка обязанностей",
                    value=[
                            {
                                "id": 67,
                                "name": "PR-деятельность и связи с общественностью",
                                "prof_area": 7
                            },
                            {
                                "id": 122,
                                "name": "PR-деятельность и связи с общественностью",
                                "prof_area": 2
                            }
                        ],
                    status_codes=[str(status.HTTP_200_OK)],
                ),
            ]
)

duty_retrieve_schema = extend_schema(
    summary="Детальная информация об обязанности",
    responses={
            status.HTTP_200_OK: DutySerializer,
            status.HTTP_400_BAD_REQUEST: DummyDetailStatusSerializer,
            status.HTTP_401_UNAUTHORIZED: DummyDetailStatusSerializer,
            status.HTTP_403_FORBIDDEN: DummyDetailStatusSerializer,
    },
    parameters=[
            OpenApiParameter(
                name='prof_area',
                location=OpenApiParameter.PATH,
                description='Параметр для поиска навыков выбранной проф.области',
                required=True,
                type=int
            ),
    ],
    examples=[
                OpenApiExample(
                    "get duties retrieve example",
                    description="Пример для get-запроса обязанности",
                    value={
                                "id": 67,
                                "name": "PR-деятельность и связи с общественностью",
                                "prof_area": 7
                            },
                    status_codes=[str(status.HTTP_200_OK)],
                ),
            ]
)
