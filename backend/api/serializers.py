from rest_framework import serializers
from django.core.exceptions import ValidationError
from django.utils import timezone
from django.shortcuts import get_object_or_404

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
    CITIZENSHIP,
    EDUCATION,
    EMPLOYMENT_TYPE,
    EMPLOYMENT_METHOD,
    MIN_EMPLOYEE_REWARD,
    PAYMENT,
    RESUME_OPTIONS,
    SCHEDULE,
)


class CitySerializer(serializers.ModelSerializer):
    """
        Сериализатор для модели город.
    """
    name = serializers.CharField(source='city.name')

    class Meta:
        model = City
        fields = ('id', 'name')


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
        fields = ('id', 'prof_area')


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
    prof_area = serializers.CharField(source='prof.prof_area')
    prof_name = serializers.CharField(source='prof.prof_name')

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
    socialPackage = serializers.PrimaryKeyRelatedField(
        queryset=SocialPackage.objects.all(), many=True)

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
    recruiterTasks = serializers.PrimaryKeyRelatedField(
        queryset=TaskRecruiter.objects.all(), many=True)
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


class RecruiterSerializer(serializers.ModelSerializer):
    """
        Сериализатор для модели требование к рекрутерам.
    """
    specialSkills = serializers.PrimaryKeyRelatedField(
        queryset=SkillRecruiter.objects.all(), many=True)
    additionalTasks = serializers.PrimaryKeyRelatedField(
        queryset=TaskAdditional.objects.all(), many=True)
    blacklistedCompanies = serializers.PrimaryKeyRelatedField(
        queryset=Company.objects.all(), many=True)

    class Meta:
        model = Recruiter
        fields = "__all__"


class InquirySerializer(serializers.ModelSerializer):
    """
        Сериализатор для модели заявки.
    """
    name = serializers.CharField()
    # prof = ProfessionSerializer()
    prof = serializers.PrimaryKeyRelatedField(
        queryset=Profession.objects.all())
    employeeResponsibilities = serializers.PrimaryKeyRelatedField(
        queryset=Duty.objects.all(), many=True)
    softwareSkills = serializers.PrimaryKeyRelatedField(
        queryset=Software.objects.all(), many=True)
    # city = CitySerializer()
    city = serializers.PrimaryKeyRelatedField(
        queryset=City.objects.all())
    salary_min = serializers.IntegerField()
    salary_max = serializers.IntegerField()
    education = serializers.ChoiceField(choices=EDUCATION)
    experience = serializers.IntegerField()
    citizenship = serializers.ChoiceField(choices=CITIZENSHIP)
    drivingLicense = serializers.BooleanField()
    carOwnership = serializers.BooleanField()

    workSchedule = serializers.ChoiceField(choices=SCHEDULE)
    workFormat = serializers.ChoiceField(choices=EMPLOYMENT_METHOD)
    contractType = serializers.ChoiceField(choices=EMPLOYMENT_TYPE)
    socialPackage = serializers.PrimaryKeyRelatedField(
        queryset=SocialPackage.objects.all(), many=True)

    employeeReward = serializers.IntegerField(min_value=MIN_EMPLOYEE_REWARD)
    paymentType = serializers.ChoiceField(choices=PAYMENT)
    employeeCount = serializers.IntegerField()
    recruiterTasks = serializers.PrimaryKeyRelatedField(
        queryset=TaskRecruiter.objects.all(), many=True)
    desiredFirstResumeDate = serializers.DateField(input_formats=['%d-%m-%Y'])
    desiredEmployeeExitDate = serializers.DateField(input_formats=['%d-%m-%Y'])
    resumeFormat = serializers.ChoiceField(choices=RESUME_OPTIONS)

    experienceYears = serializers.IntegerField()
    specialSkills = serializers.PrimaryKeyRelatedField(
        queryset=SkillRecruiter.objects.all(), many=True)
    additionalTasks = serializers.PrimaryKeyRelatedField(
        queryset=TaskAdditional.objects.all(), many=True)
    isIndividual = serializers.BooleanField()
    blacklistedCompanies = serializers.PrimaryKeyRelatedField(
        queryset=Company.objects.all(), many=True)
    recruiterCount = serializers.IntegerField()

    class Meta:
        model = Inquiry
        fields = (
            'name',
            'prof',
            'city',
            'salary_min',
            'salary_max',
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
            'desiredFirstResumeDate',
            'desiredEmployeeExitDate',
            'experienceYears',
            'specialSkills',
            'additionalTasks',
            'isIndividual',
            'blacklistedCompanies',
            'recruiterCount'
        )

    def create(self, validated_data):
        prof_data = validated_data.pop('prof').id
        city_data = validated_data.pop('city').id
        employeeResponsibilities = validated_data.pop(
            'employeeResponsibilities')
        softwareSkills = validated_data.pop('softwareSkills')
        name = validated_data.pop('name')
        salary_min = validated_data.pop('salary_min')
        salary_max = validated_data.pop('salary_max')
        # profession_id = prof_data['id']
        # city_id = city_data['id']

        description_data = {
            'education': validated_data.pop('education'),
            'experience': validated_data.pop('experience'),
            'citizenship': validated_data.pop('citizenship'),
            'drivingLicense': validated_data.pop('drivingLicense'),
            'carOwnership': validated_data.pop('carOwnership')
        }
        conditions_data = {
            'workSchedule': validated_data.pop('workSchedule'),
            'workFormat': validated_data.pop('workFormat'),
            'contractType': validated_data.pop('contractType'),
        }
        socialPackages = validated_data.pop('socialPackage')
        parnership_data = {
            'employeeReward': validated_data.pop('employeeReward'),
            'paymentType': validated_data.pop('paymentType'),
            'employeeCount': validated_data.pop('employeeCount'),
            'desiredFirstResumeDate': validated_data.pop(
                'desiredFirstResumeDate'),
            'desiredEmployeeExitDate': validated_data.pop(
                'desiredEmployeeExitDate'),
            'resumeFormat': validated_data.pop('resumeFormat')
        }
        recruiterTasks = validated_data.pop('recruiterTasks')
        recruiter_data = {
            'experienceYears': validated_data.pop('experienceYears'),
            'isIndividual': validated_data.pop('isIndividual'),
            'recruiterCount': validated_data.pop('recruiterCount'),
        }
        specialSkills = validated_data.pop('specialSkills')
        additionalTasks = validated_data.pop('additionalTasks')
        blacklistedCompanies = validated_data.pop('blacklistedCompanies')
        profession = get_object_or_404(Profession, id=prof_data)
        city = get_object_or_404(City, id=city_data)
        description_instance = Description.objects.create(**description_data)
        conditions_instance = Conditions.objects.create(**conditions_data)
        conditions_instance.socialPackage.set(socialPackages)
        parnership_instance = Partnership.objects.create(**parnership_data)
        parnership_instance.recruiterTasks.set(recruiterTasks)
        recruiter_instance = Recruiter.objects.create(**recruiter_data)
        recruiter_instance.specialSkills.set(specialSkills)
        recruiter_instance.additionalTasks.set(additionalTasks)
        recruiter_instance.blacklistedCompanies.set(blacklistedCompanies)
        inquiry_instance = Inquiry.objects.create(
            name=name,
            prof=profession, city=city,
            salary_min=salary_min,
            salary_max=salary_max,
            description=description_instance,
            conditions=conditions_instance,
            partnership=parnership_instance,
            recruiter=recruiter_instance)
        inquiry_instance.employeeResponsibilities.set(employeeResponsibilities)
        inquiry_instance.softwareSkills.set(softwareSkills)
        return inquiry_instance
    
    def to_representation(self, instance):
        return InquiryGetSerializer(instance,
                                    context=self.context).data
    # def to_representation(self, instance):
    #     data = super().to_representation(instance)
    #     if instance.prof:
    #         prof_area = instance.prof.prof_area
    #         duties = Duty.objects.filter(prof_area=prof_area)
    #         data['employeeResponsibilities'] = [duty.id for duty in duties]
    #     return data
    


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
