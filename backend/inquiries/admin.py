# from django.contrib import admin

# from .models import Location, Profession, Inquery, City


# class PositionInline(admin.TabularInline):

#     model = IngredientsRecipe
#     verbose_name = "Ингредиент"
#     verbose_name_plural = "Ингредиент"
#     min_num = 1

# class CityAdmin(admin.ModelAdmin):
#     list_display = ('id', 'name')
#     list_filter = ('name', )
#     list_editable = ('name',)
#     search_fields = ('name', )


# class LocationAdmin(admin.ModelAdmin):
#     list_display = ('id', 'name', 'city')
#     list_filter = ('city', )
#     list_editable = ('city',)
#     search_fields = ('city', )


# class ProfessionAdmin(admin.ModelAdmin):
#     list_display = ('id', 'name')
#     list_editable = ('name')


# class InqueryAdmin(admin.ModelAdmin):
#     list_display = ('id', 'title', 'location', 'profession', 'salary_low',
#                     'salary_high', 'description', 'employment', 'payment',
#                     'reward', 'resume_date', 'work_date', 'hr_number',
#                     'hr_duties', 'resume_opt', 'conditions')
#     list_editable = ('title', 'location', 'reward', 'profession',
#                      'salary_high', 'salary_low')


# admin.site.register(City, CityAdmin)
# admin.site.register(Inquery, InqueryAdmin)
# admin.site.register(Location, LocationAdmin)
# admin.site.register(Profession, ProfessionAdmin)
