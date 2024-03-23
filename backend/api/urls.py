from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import InquiryViewSet,DutyViewSet,ConditionsViewSet,ParnershipViewSet,DescriptionViewSet,RecruiterViewSet

app_name = 'api'

router = DefaultRouter()
router.register(r'inquiries', InquiryViewSet, basename='inquiries')
router.register(r'duties', DutyViewSet, basename='duties')
router.register(r'conditions', ConditionsViewSet, basename='conditions')
router.register(r'partnerships', ParnershipViewSet, basename='partnerships')
router.register(r'descriptions', DescriptionViewSet, basename='descriptions')
router.register(r'recruiters', RecruiterViewSet, basename='recruiters')

urlpatterns = [
    path('v1/', include(router.urls)),

   ]
