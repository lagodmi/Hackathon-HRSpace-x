from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import InquiryViewSet

app_name = 'api'

router = DefaultRouter()
router.register(r'inquiries', InquiryViewSet, basename='inquiries')

urlpatterns = [
    path('v1/', include(router.urls)),
]
