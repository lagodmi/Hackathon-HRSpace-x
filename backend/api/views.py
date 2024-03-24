from datetime import datetime, timezone
from rest_framework import status, viewsets, filters
from rest_framework import permissions
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema_view, extend_schema
from .filters import DutyFilter
from inquiries.constants import (
    CITIZENSHIP,
    EDUCATION,
    EMPLOYMENT_METHOD,
    EMPLOYMENT_TYPE,
    MIN_EMPLOYEE_REWARD,
    RESUME_OPTIONS,
    SCHEDULE,
    PAYMENT
)

from .serializers import (
    CitySerializer,
    ConditionsSerializer,
    DescriptionSerializer,
    DutySerializer,
    InquirySerializer,
    PartnershipSerializer,
    ProfessionAreaSerializer,
    ProfessionSerializer,
    ProfessionGetSerializer,
    InquiryGetSerializer,
    RecruiterSerializer
)
from inquiries.models import (
    Description,
    Duty,
    City,
    Company,
    Inquiry,
    Profession,
    ProfessionArea,
    Software,
    SkillRecruiter,
    SocialPackage,
    TaskAdditional,
    TaskRecruiter,
)

from .swagger import (
    inquiry_list_schema,
    inquiry_update_schema,
    inquiry_create_schema,
    inquiry_retrieve_schema,
    inquiry_delete_schema,
    duty_list_schema,
    duty_retrieve_schema,
)


def get_education_key(value):
    for key, label in EDUCATION:
        if label == value:
            return key
    return None


def get_citizenship_key(value):
    for key, label in CITIZENSHIP:
        if label == value:
            return key
    return None


def get_workSchedule_key(value):
    for key, label in SCHEDULE:
        if label == value:
            return key
    return None


def get_workFormat_key(value):
    for key, label in EMPLOYMENT_TYPE:
        if label == value:
            return key
    return None


def get_contractType_key(value):
    for key, label in EMPLOYMENT_METHOD:
        if label == value:
            return key
    return None


def get_paymentType_key(value):
    for key, label in PAYMENT:
        if label == value:
            return key
    return None


def get_resumeFormat_key(value):
    for key, label in RESUME_OPTIONS:
        if label == value:
            return key
    return None


@extend_schema(tags=["Inquiries"])
@extend_schema_view(
    list=inquiry_list_schema,
    update=inquiry_update_schema,
    create=inquiry_create_schema,
    retrieve=inquiry_retrieve_schema,
    delete=inquiry_delete_schema,)
class InquiryViewSet(viewsets.ModelViewSet):
    """
        Вьюсет для заявок.
    """
    queryset = Inquiry.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return InquiryGetSerializer
        return InquirySerializer

    def create(self, request):
        # Блок профессия.
        prof_data = request.data['prof']
        prof_area_data = prof_data['prof_area']
        try:
            profession_area = ProfessionArea.objects.get(
                name=prof_area_data
            )
            profession = Profession.objects.get(
                id=prof_data['id'],
                prof_area=profession_area,
                prof_name=prof_data['prof_name']
            )
        except Profession.DoesNotExist:
            profession_serializer = ProfessionSerializer(data=prof_data)
            if profession_serializer.is_valid():
                profession = profession_serializer.save()
            else:
                return Response(
                    {'message': 'Ошибка при создании объекта профессия.'},
                    status=status.HTTP_400_BAD_REQUEST
                )

        # Блок город.
        city_data = request.data['city']
        try:
            city = City.objects.get(id=city_data['id'],
                                    name=city_data['name'])
        except City.DoesNotExist:
            city_serializer = CitySerializer(data=city_data)
            if city_serializer.is_valid():
                city = city_serializer.save()
            else:
                return Response(
                    {'message': 'Ошибка при создании объекта город.'},
                    status=status.HTTP_400_BAD_REQUEST
                )

        # Описание.
        desc_data = {
            'education': get_education_key(request.data['education']),
            'experience': request.data['experience'],
            'citizenship': get_citizenship_key(request.data['citizenship']),
            'drivingLicense': request.data['drivingLicense'],
            'carOwnership': request.data['carOwnership']
        }

        desc_serializer = DescriptionSerializer(data=desc_data)
        if desc_serializer.is_valid():
            desc = desc_serializer.save()
        else:
            return Response(
                {'message': 'Ошибка при создании описания.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Условия работы.
        cond_data = {
            'workSchedule': get_workSchedule_key(request.data['workSchedule']),
            'workFormat': get_workFormat_key(request.data['workFormat']),
            'contractType': get_contractType_key(request.data['contractType']),
            'socialPackage': request.data['socialPackage']
        }

        cond_serializer = ConditionsSerializer(data=cond_data)
        if cond_serializer.is_valid():
            conditions = cond_serializer.save()
        else:
            return Response(
                {'message': f'Ошибка при создании условия работы. {cond_serializer.errors}'},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Условия сотрудничества.
        desired_first_resume_date = request.data['dates']['desiredFirstResumeDate']
        desired_employee_exit_date = request.data['dates']['desiredEmployeeExitDate']

        if desired_first_resume_date and desired_employee_exit_date:
            if desired_employee_exit_date <= desired_first_resume_date:
                return Response(
                    {'message': 'Дата выхода на работу должна быть позже даты получения резюме.'},
                    status=status.HTTP_400_BAD_REQUEST
                )

        partnership_data = {
            'employeeReward': request.data['employeeReward'],
            'paymentType': get_paymentType_key(request.data['paymentType']),
            'employeeCount': request.data['employeeCount'],
            'recruiterTasks': request.data['recruiterTasks'],
            'desiredFirstResumeDate': desired_first_resume_date,
            'desiredEmployeeExitDate': desired_employee_exit_date,
            'resumeFormat': get_resumeFormat_key(request.data['resumeFormat'])
        }

        partnership_serializer = PartnershipSerializer(data=partnership_data)
        if partnership_serializer.is_valid():
            partnership = partnership_serializer.save()
        else:
            return Response(
                {'message': f'Ошибка при создании условия сотрудничества. {partnership_serializer.errors}'},
                status=status.HTTP_400_BAD_REQUEST
            )


        # Требование к рекрутерам.
        recruiter_data = {
            'experienceYears': request.data['experienceYears'],
            'specialSkills': request.data['specialSkills'],
            'additionalTasks': request.data['additionalTasks'],
            'isIndividual': request.data['isIndividual'],
            'blacklistedCompanies': request.data['blacklistedCompanies'],
            'recruiterCount': request.data['recruiterCount']
        }

        recruiter_serializer = RecruiterSerializer(data=recruiter_data)
        if recruiter_serializer.is_valid():
            recruiter = recruiter_serializer.save()
        else:
            return Response(
                {'message': f'Произошла ошибка при создании объекта рекрутер. {recruiter_serializer.errors}'},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Привязка к модели Inquiry
        prof_name = request.data['prof']['prof_area']
        prof_area = ProfessionArea.objects.get(
            name=prof_name
        )
        employeeResponsibilities_data = [
            {
                'name': request.data['employeeResponsibilities'][i]['name'],
                'prof_area': prof_area.id
            } for i in range(len(request.data['employeeResponsibilities']))
        ]
        inquiry_data = {
            'name': request.data['name'],
            'prof': profession.id,
            'softwareSkills': request.data['softwareSkills'],
            'salary_min': request.data['salaryRange']['salary_min'],
            'salary_max': request.data['salaryRange']['salary_max'],
            'city': city.id,
            'employeeResponsibilities': employeeResponsibilities_data,
            'description': desc.id,
            'conditions': conditions,
            'partnership': partnership,
            'recruiter': recruiter
        }

        inquiry_serializer = InquirySerializer(data=inquiry_data)
        if inquiry_serializer.is_valid():
            inquiry = inquiry_serializer.save()
        else:
            return Response(
                {'message': f'Произошла ошибка при создании  заявки. {inquiry_serializer.errors}'},
                status=status.HTTP_400_BAD_REQUEST
            )

        return Response(InquirySerializer(inquiry).data)


@extend_schema(tags=["Duties"])
@extend_schema_view(
    list=duty_list_schema,
    retrieve=duty_retrieve_schema,)
class DutyViewSet(viewsets.ModelViewSet):
    """Вьюсет для обязанности, фильтр по названию профессии"""
    serializer_class = DutySerializer
    queryset = Duty.objects.all()
    filter_backends = (DjangoFilterBackend, )
    filterset_class = DutyFilter
