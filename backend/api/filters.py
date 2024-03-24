import django_filters

from inquiries.models import Duty


class DutyFilter(django_filters.FilterSet):
    prof_area = django_filters.CharFilter(field_name='prof_area__name',
                                          lookup_expr='icontains')

    class Meta:
        model = Duty
        fields = ['prof_area']