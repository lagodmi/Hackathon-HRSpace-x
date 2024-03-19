from django.contrib import admin


from .models import (Profession, Inquiry, City, Company,
                     Skill, Duty, Partnership, Conditions,
                     Recruiter, ProfessionArea, Description,
                     SocialPackage, TaskAdditional, SkillRecruiter,
                     TaskRecruiter)


class CityAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_filter = ('name', )
    list_editable = ('name',)
    search_fields = ('name', )


class ProfessionAreaAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_editable = ('name',)


class ProfessionAdmin(admin.ModelAdmin):
    list_display = ('id', 'prof_area', 'prof_name')
    list_editable = ('prof_area', 'prof_name')
    # filter_horizontal = ('employeeResponsibilities', 'softwareSkills')


class SkillAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_editable = ('name',)


class TaskAdditionalAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_editable = ('name',)


class SkillRecruiterAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_editable = ('name',)


class DutyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_editable = ('name',)


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_editable = ('name',)


class TaskRecruiterAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_editable = ('name',)


class DescriptionAdmin(admin.ModelAdmin):
    list_display = ('id', 'education', 'experience', 'citizenship',
                    'drivingLicense', 'carOwnership')
    list_editable = ('education', 'experience', 'citizenship',
                     'drivingLicense', 'carOwnership')


class SocialPackageAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_editable = ('name',)


class ConditionsAdmin(admin.ModelAdmin):
    list_display = ('id', 'workSchedule', 'workFormat',
                    'contractType')
    list_editable = ('workSchedule', 'workFormat',
                     'contractType')
    filter_horizontal = ('socialPackage',)


class PartnershipAdmin(admin.ModelAdmin):
    list_display = ('id', 'employeeReward', 'paymentType',
                    'employeeCount',
                    'desiredFirstResumeDate', 'desiredEmployeeExitDate',
                    'resumeFormat')
    list_editable = ('employeeReward', 'paymentType',
                     'employeeCount',
                     'desiredFirstResumeDate', 'desiredEmployeeExitDate',
                     'resumeFormat')
    filter_horizontal = ('recruiterTasks',)


class RecruiterAdmin(admin.ModelAdmin):
    list_display = ('id', 'experienceYears', 'isIndividual',
                    'recruiterCount')
    list_editable = ('experienceYears', 'isIndividual',
                     'recruiterCount')
    filter_horizontal = ('blacklistedCompanies', 'specialSkills',
                         'additionalTasks')


class InqueryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'prof', 'city', 'salary_min',
                    'salary_max', 'description', 'conditions',
                    'partnership', 'recruiter')
    list_editable = ('name', 'prof', 'city', 'salary_min',
                     'salary_max', 'description', 'conditions',
                     'partnership', 'recruiter')


admin.site.register(City, CityAdmin)
admin.site.register(Inquiry, InqueryAdmin)
admin.site.register(Profession, ProfessionAdmin)
admin.site.register(ProfessionArea, ProfessionAreaAdmin)
admin.site.register(Skill, SkillAdmin)
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
