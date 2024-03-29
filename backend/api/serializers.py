from django.utils import timezone
from rest_framework import serializers

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
    prof_area = serializers.PrimaryKeyRelatedField(
        queryset=ProfessionArea.objects.all()
    )

    class Meta:
        model = Profession
        fields = ('id', 'prof_area', 'prof_name')


class DutySerializer(serializers.ModelSerializer):
    """
        Сериализатор для модели обязанности.
    """
    prof_area = serializers.PrimaryKeyRelatedField(
        queryset=ProfessionArea.objects.all()
    )

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
        fields = '__all__'

    def create(self, validated_data):
        social_packages_data = validated_data.pop('socialPackage')
        conditions = Conditions.objects.create(**validated_data)

        for social_package_data in social_packages_data:
            soc = SocialPackage.objects.create(**social_package_data)
            conditions.socialPackage.add(soc)

        return conditions.id


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
    desiredFirstResumeDate = serializers.DateField(input_formats=['%d-%m-%Y'])
    desiredEmployeeExitDate = serializers.DateField(input_formats=['%d-%m-%Y'])

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

    def create(self, validated_data):
        recruiter_tasks_data = validated_data.pop('recruiterTasks')
        partnership = Partnership.objects.create(**validated_data)

        for recruiter_task_data in recruiter_tasks_data:
            task = TaskRecruiter.objects.create(**recruiter_task_data)
            partnership.recruiterTasks.add(task)

        return partnership.id


class RecruiterSerializer(serializers.ModelSerializer):
    """
        Сериализатор для модели требование к рекрутерам.
    """
    specialSkills = SkillRecruiterSerializer(many=True)
    additionalTasks = TaskAdditionalSerializer(many=True)
    blacklistedCompanies = CompanySerializer(many=True)

    class Meta:
        model = Recruiter
        fields = "__all__"

    def create(self, validated_data):
        special_skills_data = validated_data.pop('specialSkills')
        additional_tasks_data = validated_data.pop('additionalTasks')
        blacklisted_companies_data = validated_data.pop('blacklistedCompanies')
        recruiter = Recruiter.objects.create(**validated_data)

        for special_skill_data in special_skills_data:
            skill = SkillRecruiter.objects.create(**special_skill_data)
            recruiter.specialSkills.add(skill)

        for additional_task_data in additional_tasks_data:
            task = TaskAdditional.objects.create(**additional_task_data)
            recruiter.additionalTasks.add(task)

        for blacklisted_company_data in blacklisted_companies_data:
            company = Company.objects.create(**blacklisted_company_data)
            recruiter.blacklistedCompanies.add(company)

        return recruiter.id


class InquirySerializer(serializers.ModelSerializer):
    """
        Сериализатор для модели заявки.
    """
    prof = serializers.PrimaryKeyRelatedField(
        queryset=Profession.objects.all()
    )
    employeeResponsibilities = DutySerializer(many=True)
    softwareSkills = SoftwareSerializer(many=True)
    city = serializers.PrimaryKeyRelatedField(queryset=City.objects.all())
    description = serializers.PrimaryKeyRelatedField(
        queryset=Description.objects.all()
    )
    conditions = serializers.PrimaryKeyRelatedField(
        queryset=Conditions.objects.all()
    )
    partnership = serializers.PrimaryKeyRelatedField(
        queryset=Partnership.objects.all()
    )
    recruiter = serializers.PrimaryKeyRelatedField(
        queryset=Recruiter.objects.all()
    )

    class Meta:
        model = Inquiry
        fields = "__all__"

    def create(self, validated_data):
        employee_responsibilities_data = validated_data.pop(
            'employeeResponsibilities'
        )
        software_skills_data = validated_data.pop('softwareSkills')
        inquiry = Inquiry.objects.create(**validated_data)

        for employee_responsibilitie_data in employee_responsibilities_data:
            duty = Duty.objects.create(**employee_responsibilitie_data)
            inquiry.employeeResponsibilities.add(duty)

        for software_skill_data in software_skills_data:
            software = Software.objects.create(**software_skill_data)
            inquiry.softwareSkills.add(software)

        return inquiry


# Сериализаторы на GET запросы.


class ProfessionGetSerializer(serializers.ModelSerializer):
    prof_area = serializers.CharField(source='prof_area.name')

    class Meta:
        model = Profession
        fields = ('id', 'prof_area', 'prof_name')


class CityGetSerializer(serializers.ModelSerializer):
    """
        Сериализатор для модели город.
    """
    id = serializers.CharField()

    class Meta:
        model = City
        fields = "__all__"


class InquiryGetSerializer(serializers.ModelSerializer):
    """
        Сериализатор для модели заявки.
    """
    prof = ProfessionGetSerializer()
    city = CityGetSerializer()
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
        return [{'name': odject.name}
                for odject in obj.employeeResponsibilities.all()]

    def get_education(self, obj):
        return obj.description.get_education_display()

    def get_citizenship(self, obj):
        return obj.description.get_citizenship_display()

    def get_softwareSkills(self, obj):
        return [{'name': odject.name} for odject in obj.softwareSkills.all()]

    def get_workSchedule(self, obj):
        return obj.conditions.get_workSchedule_display()

    def get_workFormat(self, obj):
        return obj.conditions.get_workFormat_display()

    def get_contractType(self, obj):
        return obj.conditions.get_contractType_display()

    def get_socialPackage(self, obj):
        return [{'name': odject.name}
                for odject in obj.conditions.socialPackage.all()]

    def get_paymentType(self, obj):
        return obj.partnership.get_paymentType_display()

    def get_recruiterTasks(self, obj):
        return [{'name': odject.name}
                for odject in obj.partnership.recruiterTasks.all()]

    def get_resumeFormat(self, obj):
        return obj.partnership.get_resumeFormat_display()

    def get_dates(self, obj):
        return {
            'desiredFirstResumeDate':
            obj.partnership.desiredFirstResumeDate.strftime('%d-%m-%Y'),

            'desiredEmployeeExitDate':
            obj.partnership.desiredEmployeeExitDate.strftime('%d-%m-%Y')
        }

    def get_specialSkills(self, obj):
        return [{'name': odject.name}
                for odject in obj.recruiter.specialSkills.all()]

    def get_additionalTasks(self, obj):
        return [{'name': odject.name}
                for odject in obj.recruiter.additionalTasks.all()]

    def get_blacklistedCompanies(self, obj):
        return [{'name': odject.name}
                for odject in obj.recruiter.blacklistedCompanies.all()]

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
