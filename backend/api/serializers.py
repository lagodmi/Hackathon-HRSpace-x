from rest_framework import serializers
from django.core.exceptions import ValidationError
from django.utils import timezone

from inquiries.constants import MIN_EMPLOYEE_REWARD
from inquiries.models import (
    City,
    Company,
    Conditions,
    Description,
    Duty,
    Inquiry,
    Partnership,
    Profession,
    ProfessionArea,
    Recruiter,
    SkillRecruiter,
    Software,
    SocialPackage,
    TaskAdditional,
    TaskRecruiter,
)


class CitySerializer(serializers.ModelSerializer):
    """
        Сериализатор для модели город.
    """

    class Meta:
        model = City
        fields = "__all__"


class CompanySerializer(serializers.ModelSerializer):
    """
        Сериализатор для модели компании.
    """

    class Meta:
        model = Company
        fields = "__all__"


class ProfessionAreaSerializer(serializers.ModelSerializer):
    """
        Сериализатор для модели профессиональной области.
    """

    class Meta:
        model = ProfessionArea
        fields = "__all__"


class SkillRecruiterSerializer(serializers.ModelSerializer):
    """
        Сериализатор для модели навыки рекрутера.
    """

    class Meta:
        model = SkillRecruiter
        fields = "__all__"


class SocialPackageSerializer(serializers.ModelSerializer):
    """
        Сериализатор для модели социального пакета.
    """

    class Meta:
        model = SocialPackage
        fields = "__all__"


class TaskAdditionalSerializer(serializers.ModelSerializer):
    """
        Сериализатор для модели дополнительные задачи.
    """

    class Meta:
        model = TaskAdditional
        fields = "__all__"


class TaskRecruiterSerializer(serializers.ModelSerializer):
    """
        Сериализатор для модели задачи рекрутера.
    """

    class Meta:
        model = TaskRecruiter
        fields = "__all__"


class ProfessionSerializer(serializers.ModelSerializer):
    """
        Сериализатор для модели профессии.
    """
    prof_area = ProfessionAreaSerializer()

    class Meta:
        model = Profession
        fields = ('id', 'prof_area', 'prof_name')


class DutySerializer(serializers.ModelSerializer):
    """
        Сериализатор для модели обязанности.
    """
    prof_area = ProfessionAreaSerializer()

    class Meta:
        model = Duty
        fields = ('id', 'name', 'prof_area')


class SoftwareSerializer(serializers.ModelSerializer):
    """
        Сериализатор для модели навыка.
    """

    class Meta:
        model = Software
        fields = "__all__"


class ConditionsSerializer(serializers.ModelSerializer):
    """
        Сериализатор для модели условия работы.
    """
    socialPackage = SocialPackageSerializer(many=True)

    class Meta:
        model = Conditions
        fields = "__all__"


class DescriptionSerializer(serializers.ModelSerializer):
    """
        Сериализатор для модели описание вакансии.
    """

    class Meta:
        model = Description
        fields = "__all__"


class PartnershipSerializer(serializers.ModelSerializer):
    """
        Сериализатор для модели условия сотрудничества.
    """
    recruiterTasks = TaskRecruiterSerializer(many=True)
    employeeReward = serializers.IntegerField(min_value=MIN_EMPLOYEE_REWARD)
    desiredFirstResumeDate = serializers.DateField()
    desiredEmployeeExitDate = serializers.DateField()

    class Meta:
        model = Partnership
        fields = "__all__"

    def validate(self, data):
        if data['desiredFirstResumeDate'] <= timezone.now().date():
            raise serializers.ValidationError(
                {'desiredFirstResumeDate': 'Дата получения резюме не может'
                                           'быть раньше сегодняшней даты.'})
        if data['desiredFirstResumeDate'] > data['desiredEmployeeExitDate']:
            raise serializers.ValidationError(
                {'desiredEmployeeExitDate': 'Дата выхода на работу должна быть'
                                            'позже даты получения резюме.'})
        return data


class RecruiterSerializer(serializers.ModelSerializer):
    """
        Сериализатор для модели требование к рекрутерам.
    """
    specialSkills = SkillRecruiterSerializer()
    additionalTasks = TaskAdditionalSerializer()
    blacklistedCompanies = CompanySerializer()

    class Meta:
        model = Recruiter
        fields = "__all__"


class InquirySerializer(serializers.ModelSerializer):
    """
        Сериализатор для модели заявки.
    """
    prof = ProfessionSerializer()
    employeeResponsibilities = DutySerializer(many=True)
    softwareSkills = SoftwareSerializer(many=True)
    city = CitySerializer()
    description = DescriptionSerializer()
    conditions = ConditionsSerializer()
    partnership = PartnershipSerializer()
    recruiter = RecruiterSerializer()

    class Meta:
        model = Inquiry
        fields = "__all__"
