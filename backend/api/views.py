from rest_framework import status, viewsets, filters
from rest_framework import permissions
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from .serializers import (
    CitySerializer,
    InquirySerializer,
    ProfessionAreaSerializer,
    ProfessionSerializer,
    ProfessionGetSerializer,
    InquiryGetSerializer
)
from inquiries.models import (
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
        prof_data = request.data.get('prof')
        prof_area_data = prof_data.pop('prof_area')
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
        city_data = request.data.get('city')
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





        # Привязка к модели Inquiry
        Inquiry.objects.create(prof=profession,
                               city=city)
