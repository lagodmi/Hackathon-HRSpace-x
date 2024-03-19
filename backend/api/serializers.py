from rest_framework import serializers

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
    Skill,
    SkillRecruiter,
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
    profession = ProfessionSerializer()

    class Meta:
        model = Duty
        fields = ('id', 'name', 'profession')


class SkillSerializer(serializers.ModelSerializer):
    """
        Сериализатор для модели навыка.
    """
    profession = ProfessionSerializer()

    class Meta:
        model = Skill
        fields = ('id', 'name', 'profession')








# class ConditionsSerializer(serializers.ModelSerializer):
#     """
#         Сериализатор для модели условия работы.
#     """

#     class Meta:
#         model = Conditions
#         fields = "__all__"


# class DescriptionSerializer(serializers.ModelSerializer):
#     """
#         Сериализатор для модели описание вакансии.
#     """

#     class Meta:
#         model = Description
#         fields = "__all__"


# class InquirySerializer(serializers.ModelSerializer):
#     """
#         Сериализатор для модели заявки.
#     """

#     class Meta:
#         model = Inquiry
#         fields = "__all__"


# class PartnershipSerializer(serializers.ModelSerializer):
#     """
#         Сериализатор для модели условия сотрудничества.
#     """

#     class Meta:
#         model = Partnership
#         fields = "__all__"


# class RecruiterSerializer(serializers.ModelSerializer):
#     """
#         Сериализатор для модели требование к рекрутерам.
#     """

#     class Meta:
#         model = Recruiter
#         fields = "__all__"
