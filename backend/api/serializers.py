from rest_framework import serializers
from django.core.exceptions import ValidationError
from django.utils import timezone

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
from inquiries.constants import (
    EMPLOYMENT_METHOD,
    MIN_EMPLOYEE_REWARD,
    PAYMENT,
    RESUME_OPTIONS,
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
    desiredFirstResumeDate = serializers.DateField(format="%d-%m-%Y")
    desiredEmployeeExitDate = serializers.DateField(format="%d-%m-%Y")

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

# Сериализаторы на GET запросы.


class ProfessionGetSerializer(serializers.ModelSerializer):
    prof_area = serializers.CharField(source='prof_area.name')

    class Meta:
        model = Profession
        fields = ('id', 'prof_area', 'prof_name')


class InquiryGetSerializer(serializers.ModelSerializer):
    """
        Сериализатор для модели заявки.
    """
    prof = ProfessionGetSerializer()
    city = CitySerializer()
    salaryRange = serializers.SerializerMethodField()
    employeeResponsibilities = serializers.SerializerMethodField()
    education = serializers.SerializerMethodField(source='description')
    experience = serializers.IntegerField(source='description.experience')
    citizenship = serializers.SerializerMethodField(source='description')
    softwareSkills = serializers.SerializerMethodField()
    drivingLicense = serializers.BooleanField(
        source='description.drivingLicense'
    )
    carOwnership = serializers.BooleanField(source='description.carOwnership')
    workSchedule = serializers.SerializerMethodField(source='conditions')
    workFormat = serializers.SerializerMethodField(source='conditions')
    contractType = serializers.SerializerMethodField(source='conditions')
    socialPackage = serializers.SerializerMethodField()
    employeeReward = serializers.IntegerField(
        source='partnership.employeeReward'
    )
    paymentType = serializers.SerializerMethodField(source='partnership')
    employeeCount = serializers.IntegerField(
        source='partnership.employeeCount'
    )
    recruiterTasks = serializers.SerializerMethodField()
    resumeFormat = serializers.SerializerMethodField(source='partnership')
    dates = serializers.SerializerMethodField()
    experienceYears = serializers.IntegerField(
        source='recruiter.experienceYears'
    )
    specialSkills = serializers.SerializerMethodField(source='recruiter')
    additionalTasks = serializers.SerializerMethodField(source='recruiter')
    isIndividual = serializers.BooleanField(source='recruiter.isIndividual')
    blacklistedCompanies = serializers.SerializerMethodField(
        source='recruiter'
    )
    recruiterCount = serializers.IntegerField(
        source='recruiter.recruiterCount'
    )

    def get_salaryRange(self, obj):
        return {
            'salary_min': obj.salary_min,
            'salary_max': obj.salary_max
        }

    def get_employeeResponsibilities(self, obj):
        return [duty.name for duty in obj.employeeResponsibilities.all()]

    def get_education(self, obj):
        return obj.description.get_education_display()

    def get_citizenship(self, obj):
        return obj.description.get_citizenship_display()

    def get_softwareSkills(self, obj):
        return [duty.name for duty in obj.softwareSkills.all()]

    def get_workSchedule(self, obj):
        return obj.conditions.get_workSchedule_display()

    def get_workFormat(self, obj):
        return obj.conditions.get_workFormat_display()

    def get_contractType(self, obj):
        return obj.conditions.get_contractType_display()

    def get_socialPackage(self, obj):
        return [duty.name for duty in obj.conditions.socialPackage.all()]

    def get_paymentType(self, obj):
        return obj.partnership.get_paymentType_display()

    def get_recruiterTasks(self, obj):
        return [duty.name for duty in obj.partnership.recruiterTasks.all()]

    def get_resumeFormat(self, obj):
        return obj.partnership.get_resumeFormat_display()

    def get_dates(self, obj):
        return {
            'desiredFirstResumeDate': obj.partnership.desiredFirstResumeDate.strftime('%d-%m-%Y'),
            'desiredEmployeeExitDate': obj.partnership.desiredEmployeeExitDate.strftime('%d-%m-%Y')
        }

    def get_specialSkills(self, obj):
        return [duty.name for duty in obj.recruiter.specialSkills.all()]

    def get_additionalTasks(self, obj):
        return [duty.name for duty in obj.recruiter.additionalTasks.all()]

    def get_blacklistedCompanies(self, obj):
        return [duty.name for duty in obj.recruiter.blacklistedCompanies.all()]

    class Meta:
        model = Inquiry
        fields = (
            'name',
            'prof',
            'city',
            'salaryRange',
            'employeeResponsibilities',
            'education',
            'experience',
            'citizenship',
            'softwareSkills',
            'drivingLicense',
            'carOwnership',
            'workSchedule',
            'workFormat',
            'contractType',
            'socialPackage',
            'employeeReward',
            'paymentType',
            'employeeCount',
            'recruiterTasks',
            'resumeFormat',
            'dates',
            'experienceYears',
            'specialSkills',
            'additionalTasks',
            'isIndividual',
            'blacklistedCompanies',
            'recruiterCount'
        )
