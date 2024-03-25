from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import InquiryViewSet,DutyViewSet

app_name = 'api'

router = DefaultRouter()
router.register(r'inquiries', InquiryViewSet, basename='inquiries')
router.register(r'duties', DutyViewSet, basename='duties')

urlpatterns = [
    path('v1/', include(router.urls)),
]
