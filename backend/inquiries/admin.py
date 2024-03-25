from django.contrib import admin


from .models import (
    Profession,
    Inquiry,
    City,
    Company,
    Software,
    Duty,
    Partnership,
    Conditions,
    Recruiter,
    ProfessionArea,
    Description,
    SocialPackage,
    TaskAdditional,
    SkillRecruiter,
    TaskRecruiter,
)


class CityAdmin(admin.ModelAdmin):
    """
        Админка для модели 'Город'.
    """
    list_display = ("id", "name")
    list_filter = ("name",)
    list_editable = ("name",)
    search_fields = ("name",)


class ProfessionAreaAdmin(admin.ModelAdmin):
    """
        Админка для модели 'Профессиональной области'.
    """
    list_display = ("id", "name")
    list_editable = ("name",)


class ProfessionAdmin(admin.ModelAdmin):
    """
        Админка для модели 'Профессии'.
    """
    list_display = ("id", "prof_area", "prof_name")
    list_editable = ("prof_area", "prof_name")


class SoftwareAdmin(admin.ModelAdmin):
    """
        Админка для модели 'Знание программ'.
    """
    list_display = ("id", "name")
    list_editable = ("name",)


class TaskAdditionalAdmin(admin.ModelAdmin):
    """
        Админка для модели 'Дополнительных задач'.
    """
    list_display = ("id", "name")
    list_editable = ("name",)


class SkillRecruiterAdmin(admin.ModelAdmin):
    """
        Админка для модели 'Навыки рекрутера'.
    """
    list_display = ("id", "name")
    list_editable = ("name",)


class DutyAdmin(admin.ModelAdmin):
    """
        Админка для модели 'Обязанности'.
    """
    list_display = ("id", "name")
    list_editable = ("name",)


class CompanyAdmin(admin.ModelAdmin):
    """
        Админка для модели 'Компании'.
    """
    list_display = ("id", "name")
    list_editable = ("name",)


class TaskRecruiterAdmin(admin.ModelAdmin):
    """
        Админка для модели 'Задачи рекрутера'.
    """
    list_display = ("id", "name")
    list_editable = ("name",)


class DescriptionAdmin(admin.ModelAdmin):
    """
        Админка для модели 'Описание'.
    """
    list_display = (
        "id",
        "education",
        "experience",
        "citizenship",
        "drivingLicense",
        "carOwnership",
    )
    list_editable = (
        "education",
        "experience",
        "citizenship",
        "drivingLicense",
        "carOwnership",
    )


class SocialPackageAdmin(admin.ModelAdmin):
    """
        Админка для модели 'Соц. покет'.
    """
    list_display = ("id", "name")
    list_editable = ("name",)


class ConditionsAdmin(admin.ModelAdmin):
    """
        Админка для модели 'Условия'.
    """
    list_display = ("id", "workSchedule", "workFormat", "contractType")
    list_editable = ("workSchedule", "workFormat", "contractType")
    filter_horizontal = ("socialPackage",)


class PartnershipAdmin(admin.ModelAdmin):
    """
        Админка для модели 'Сотрудничества'.
    """
    list_display = (
        "id",
        "employeeReward",
        "paymentType",
        "employeeCount",
        "desiredFirstResumeDate",
        "desiredEmployeeExitDate",
        "resumeFormat",
    )
    list_editable = (
        "employeeReward",
        "paymentType",
        "employeeCount",
        "desiredFirstResumeDate",
        "desiredEmployeeExitDate",
        "resumeFormat",
    )
    filter_horizontal = ("recruiterTasks",)


class RecruiterAdmin(admin.ModelAdmin):
    """
        Админка для модели 'Рекрутер'.
    """
    list_display = ("id", "experienceYears", "isIndividual", "recruiterCount")
    list_editable = ("experienceYears", "isIndividual", "recruiterCount")
    filter_horizontal = (
        "blacklistedCompanies",
        "specialSkills",
        "additionalTasks"
    )


class InquiryAdmin(admin.ModelAdmin):
    """
        Админка для модели 'Заявка'.
    """
    list_display = (
        "id",
        "name",
        "prof",
        "city",
        "salary_min",
        "salary_max",
        "description",
        "conditions",
        "partnership",
        "recruiter",
    )
    list_editable = (
        "name",
        "prof",
        "city",
        "salary_min",
        "salary_max",
        "description",
        "conditions",
        "partnership",
        "recruiter",
    )


admin.site.register(City, CityAdmin)
admin.site.register(Inquiry, InquiryAdmin)
admin.site.register(Profession, ProfessionAdmin)
admin.site.register(ProfessionArea, ProfessionAreaAdmin)
admin.site.register(Software, SoftwareAdmin)
admin.site.register(Duty, DutyAdmin)
admin.site.register(Description, DescriptionAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Conditions, ConditionsAdmin)
admin.site.register(SocialPackage, SocialPackageAdmin)
admin.site.register(Partnership, PartnershipAdmin)
admin.site.register(Recruiter, RecruiterAdmin)
admin.site.register(SkillRecruiter, SkillRecruiterAdmin)
admin.site.register(TaskAdditional, TaskAdditionalAdmin)
admin.site.register(TaskRecruiter, TaskRecruiterAdmin)
