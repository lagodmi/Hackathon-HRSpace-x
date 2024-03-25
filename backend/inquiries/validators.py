from django.core.exceptions import ValidationError
from django.utils import timezone


def validate_desiredFirstResumeDate_date(value):
    if value <= timezone.now().date():
        raise ValidationError(
            'Дата получения резюме не может быть раньше сегодняшней даты.'
        )


def validate_desiredEmployeeExitDate_date(value, instance):
    if value <= instance.desiredFirstResumeDate:
        raise ValidationError(
            'Дата выхода на работу должна быть позже даты получения резюме.'
        )
