from drf_spectacular.utils import extend_schema, OpenApiExample
from rest_framework import permissions, serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import InquiryGetSerializer


class DummyDetailStatusSerializer(serializers.Serializer):
    status = serializers.IntegerField()
    details = serializers.CharField()


responses_exmpl = {
            status.HTTP_200_OK: InquiryGetSerializer,
            status.HTTP_400_BAD_REQUEST: DummyDetailStatusSerializer,
            status.HTTP_401_UNAUTHORIZED: DummyDetailStatusSerializer,
            status.HTTP_403_FORBIDDEN: DummyDetailStatusSerializer,
    }

inquiry_list_schema = extend_schema(
    summary="Получить список заявок",
    responses=responses_exmpl,
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
    responses=responses_exmpl
)

inquiry_create_schema = extend_schema(
    summary="Создание новой заявки",
    responses=responses_exmpl
)

inquiry_retrieve_schema = extend_schema(
    summary="Детальная информация о заявке",
    responses=responses_exmpl
)

inquiry_delete_schema = extend_schema(
    summary="Удаление заявки",
    responses=responses_exmpl
)


# # class ExampleSerializer(serializers.Serializer):
# #     name = serializers.CharField()
# #     prof = serializers.DictField()
# #     city = serializers.DictField()
# #     salaryRange = serializers.DictField()
# #     employeeResponsibilities = serializers.ListField(
# #         child=serializers.CharField())
# #     education = serializers.CharField()
# #     experience = serializers.IntegerField()
# #     citizenship = serializers.CharField()
# #     softwareSkills = serializers.ListField(child=serializers.CharField())
# #     drivingLicense = serializers.BooleanField()
# #     carOwnership = serializers.BooleanField()
# #     workSchedule = serializers.CharField()
# #     workFormat = serializers.CharField()
# #     contractType = serializers.CharField()
# #     socialPackage = serializers.ListField(child=serializers.CharField())
# #     employeeReward = serializers.IntegerField()
# #     paymentType = serializers.CharField()
# #     employeeCount = serializers.IntegerField()
# #     recruiterTasks = serializers.ListField(child=serializers.CharField())
# #     resumeFormat = serializers.CharField()
# #     dates = serializers.DictField()
# #     experienceYears = serializers.IntegerField()
# #     specialSkills = serializers.ListField(child=serializers.CharField())
# #     additionalTasks = serializers.ListField(child=serializers.CharField())
# #     isIndividual = serializers.BooleanField()
# #     blacklistedCompanies = serializers.ListField(child=serializers.CharField())
# #     recruiterCount = serializers.IntegerField()


# @swagger_auto_schema(request_body=openapi.Schema(
#     type=openapi.TYPE_OBJECT,
    
# ))
# # class ExampleAPIView(APIView):
# #     serializer_class = ExampleSerializer

# #     def get(self, request):
# #         serializer = self.serializer_class(data=request.data)
# #         if serializer.is_valid():
# #             return Response(serializer.validated_data,
# #                             status=status.HTTP_200_OK)
# #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class ExampleRequestBodyInspector(FieldInspector):
#     def process_result(self, result, method_name, obj, **kwargs):
#         result = super().process_result(result, method_name, obj, **kwargs)
#         if method_name == 'get':
#             result['request_body'] = openapi.Schema(
#                 type=openapi.TYPE_OBJECT,
#                 properties={
#         'name': openapi.Schema(type=openapi.TYPE_STRING, example='Автомойщик'),
#         'prof': openapi.Schema(type=openapi.TYPE_OBJECT, properties={
#             'id': openapi.Schema(type=openapi.TYPE_INTEGER, example=239),
#             'prof_area': openapi.Schema(type=openapi.TYPE_STRING,
#                                         example='Автомобильный бизнес'),
#             'prof_name': openapi.Schema(type=openapi.TYPE_STRING,
#                                         example='Автомойщик'),
#         }),
#         'city': openapi.Schema(type=openapi.TYPE_OBJECT, properties={
#             'id': openapi.Schema(type=openapi.TYPE_INTEGER, example=21),
#             'name': openapi.Schema(type=openapi.TYPE_STRING,
#                                    example='Красноярск'),
#         }),
#         'salaryRange': openapi.Schema(type=openapi.TYPE_OBJECT, properties={
#             'salary_min': openapi.Schema(type=openapi.TYPE_INTEGER,
#                                          example=111111),
#             'salary_max': openapi.Schema(type=openapi.TYPE_INTEGER,
#                                          example=222222),
#         }),
#         'employeeResponsibilities': openapi.Schema(
#             type=openapi.TYPE_ARRAY,
#             items=openapi.Items(type=openapi.TYPE_STRING),
#             example=['PR-деятельность и связи с общественностью',
#                      'Активные продажи']),
#         'education': openapi.Schema(type=openapi.TYPE_STRING,
#                                     example='Неоконченное высшее'),
#         'experience': openapi.Schema(type=openapi.TYPE_INTEGER, example=3),
#         'citizenship': openapi.Schema(type=openapi.TYPE_STRING,
#                                       example='Россия'),
#         'softwareSkills': openapi.Schema(
#             type=openapi.TYPE_ARRAY,
#             items=openapi.Items(type=openapi.TYPE_STRING),
#             example=['MS Office', 'Photoshop']),
#         'drivingLicense': openapi.Schema(type=openapi.TYPE_BOOLEAN,
#                                          example=True),
#         'carOwnership': openapi.Schema(type=openapi.TYPE_BOOLEAN,
#                                        example=False),
#         'workSchedule': openapi.Schema(type=openapi.TYPE_STRING,
#                                        example='Полный рабочий день'),
#         'workFormat': openapi.Schema(type=openapi.TYPE_STRING,
#                                      example='Удаленная работа'),
#         'contractType': openapi.Schema(type=openapi.TYPE_STRING, 
#                                        example='Постоянная'),
#         'socialPackage': openapi.Schema(
#             type=openapi.TYPE_ARRAY,
#             items=openapi.Items(type=openapi.TYPE_STRING),
#             example=['Медицинское страхование', 'Отпускные']),
#         'employeeReward': openapi.Schema(type=openapi.TYPE_INTEGER,
#                                          example=50000),
#         'paymentType': openapi.Schema(type=openapi.TYPE_STRING,
#                                       example='Ежемесячно'),
#         'employeeCount': openapi.Schema(type=openapi.TYPE_INTEGER,
#                                         example=10),
#         'recruiterTasks': openapi.Schema(
#             type=openapi.TYPE_ARRAY,
#             items=openapi.Items(type=openapi.TYPE_STRING),
#             example=['Подбор персонала', 'Собеседования']),
#         'resumeFormat': openapi.Schema(type=openapi.TYPE_STRING,
#                                        example='PDF'),
#         'dates': openapi.Schema(type=openapi.TYPE_OBJECT, properties={
#             'start_date': openapi.Schema(type=openapi.TYPE_STRING,
#                                          format=openapi.FORMAT_DATE, example='2022-01-01'),
#             'end_date': openapi.Schema(type=openapi.TYPE_STRING,
#                                        format=openapi.FORMAT_DATE, example='2022-12-31'),
#         }),
#         'experienceYears': openapi.Schema(type=openapi.TYPE_INTEGER, example=5),
#         'specialSkills': openapi.Schema(
#             type=openapi.TYPE_ARRAY,
#             items=openapi.Items(type=openapi.TYPE_STRING),
#             example=['Английский язык', 'Водительские права категории B']),
#         'additionalTasks': openapi.Schema(
#             type=openapi.TYPE_ARRAY,
#             items=openapi.Items(type=openapi.TYPE_STRING),
#             example=['Управление проектами', 'Организация мероприятий']),
#         'isIndividual': openapi.Schema(type=openapi.TYPE_BOOLEAN,
#                                        example=False),
#         'blacklistedCompanies': openapi.Schema(
#             type=openapi.TYPE_ARRAY,
#             items=openapi.Items(type=openapi.TYPE_STRING),
#             example=['Company A', 'Company B']),
#         'recruiterCount': openapi.Schema(type=openapi.TYPE_INTEGER, example=2),
#     },
#     required=['__all__']
#             )
#         return result


# schema_view = get_schema_view(
#     openapi.Info(
#         title="Your API",
#         default_version='v1',
#         description="Description of your API",
#         terms_of_service="https://www.example.com/policies/terms/",
#         contact=openapi.Contact(email="contact@example.com"),
#         license=openapi.License(name="BSD License"),
#     ),
#     public=True,
#     permission_classes=(permissions.AllowAny,),
#     inspector=ExampleRequestBodyInspector
