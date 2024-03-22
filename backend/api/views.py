from rest_framework import status, viewsets, filters
from rest_framework import permissions
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from .serializers import (
    CitySerializer,
    DescriptionSerializer,
    DutySerializer,
    InquirySerializer,
    ProfessionAreaSerializer,
    ProfessionSerializer,
    ProfessionGetSerializer,
    InquiryGetSerializer
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


class InquiryViewSet(viewsets.ModelViewSet):
    """
        Вьюсет для заявок.
    """
    queryset = Inquiry.objects.all()
    # serializer_class = InquirySerializer
    # pagination_class = CustomPaginator
    # permission_classes = (IsAuthorStaffOrReadOnly,)
    # filter_backends = (DjangoFilterBackend, )
    # filterset_class = RecipeFilter

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
                return Response(profession_serializer.errors,
                                status=status.HTTP_400_BAD_REQUEST)

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
                return Response(city_serializer.errors,
                                status=status.HTTP_400_BAD_REQUEST)

        # Описание.
        desc_data = {
            'education': request.data['education'],
            'experience': request.data['experience'],
            'citizenship': request.data['citizenship'],
            'drivingLicense': request.data['drivingLicense'],
            'carOwnership': request.data['carOwnership']
        }

        desc_serializer = DescriptionSerializer(data=desc_data)
        if desc_serializer.is_valid():
            desc = desc_serializer.save()
        else:
            return Response(desc_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # Условия работы.
        cond_data = {
            'workSchedule': request.data['workSchedule'],
            'workFormat': request.data['workFormat'],
            'contractType': request.data['contractType'],
            'socialPackage': request.data['socialPackage']
        }

        cond_serializer = DescriptionSerializer(data=cond_data)
        if cond_serializer.is_valid():
            conditions = desc_serializer.save()
        else:
            return Response(cond_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # Условия сотрудничества.
        partnership_data = {
            'employeeReward': request.data['employeeReward'],
            'paymentType': request.data['paymentType'],
            'employeeCount': request.data['employeeCount'],
            'recruiterTasks': request.data['recruiterTasks'],
            'desiredFirstResumeDate': request.data['desiredFirstResumeDate'],
            'desiredEmployeeExitDate': request.data['desiredEmployeeExitDate'],
            'resumeFormat': request.data['resumeFormat']
        }

        partnership_serializer = DescriptionSerializer(data=partnership_data)
        if partnership_serializer.is_valid():
            partnership = desc_serializer.save()
        else:
            return Response(cond_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # Требование к рекрутерам.
        recruiter_data = {
            'experienceYears': request.data['experienceYears'],
            'specialSkills': request.data['specialSkills'],
            'additionalTasks': request.data['additionalTasks'],
            'isIndividual': request.data['isIndividual'],
            'blacklistedCompanies': request.data['blacklistedCompanies'],
            'recruiterCount': request.data['recruiterCount']
        }

        recruiter_serializer = DescriptionSerializer(data=recruiter_data)
        if recruiter_serializer.is_valid():
            recruiter = desc_serializer.save()
        else:
            return Response(cond_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # Привязка к модели Inquiry
        inquiry_data = {
            'name': request.data['name'],
            'prof': profession,
            'salary_min': request.data['salaryRange']['salary_min'],
            'salary_max': request.data['salaryRange']['salary_max'],
            'city': city,
            'employeeResponsibilities': request.data['employeeResponsibilities'],
            'description': desc,
            'conditions': conditions,
            'partnership': partnership,
            'recruiter': recruiter
        }

        inquiry_serializer = InquirySerializer(data=inquiry_data)
        if inquiry_serializer.is_valid():
            inquiry = inquiry_serializer.save()
        else:
            return Response(inquiry_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response(InquirySerializer(inquiry).data)
