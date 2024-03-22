from rest_framework import status, viewsets, filters
from rest_framework import permissions
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from .serializers import (
    CitySerializer,
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
        if self.request.method in permissions.SAFE_METHODS:
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
            
        # Описание.
        description_data = 

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

        inquiry_data = {
            'name': request.data['name'],
            'prof': profession,
            'salary_min': request.data['salaryRange']['salary_min'],
            'salary_max': request.data['salaryRange']['salary_max'],
            'city': city,
            'employeeResponsibilities': request.data['employeeResponsibilities']
        }

        inquiry_serializer = InquirySerializer(data=inquiry_data)
        if inquiry_serializer.is_valid():
            inquiry = inquiry_serializer.save()
        else:
            return Response(inquiry_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response(InquirySerializer(inquiry).data)

        # Привязка к модели Inquiry
        # inquiry = Inquiry.objects.create(
        #     name=request.data['name'],
        #     prof=profession,
        #     salary_min=request.data['salaryRange']['salary_min'],
        #     salary_max=request.data['salaryRange']['salary_max'],
        #     employeeResponsibilities=request.data['employeeResponsibilities'],
        #     city=city
        # )
        # inquiry.employeeResponsibilities.set(employee_responsibilities)
