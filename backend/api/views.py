from rest_framework import status, viewsets, filters
from rest_framework import permissions
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from .serializers import (InquirySerializer)
from inquiries.models import (Inquiry)


class InquiryViewSet(viewsets.ModelViewSet):
    """
    Вьюсет для для заявок.
    """
    queryset = Inquiry.objects.all()
    # pagination_class = CustomPaginator
    # permission_classes = (IsAuthorStaffOrReadOnly,)
    # filter_backends = (DjangoFilterBackend, )
    # filterset_class = RecipeFilter