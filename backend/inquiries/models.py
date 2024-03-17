from django.db import models
from django.forms import ValidationError
from .constants import (
    CITIZENSHIP,
    EDUCATION,
    EMPLOYMENT_TYPE,
    EMPLOYMENT_METHOD,
    PAYMENT,
    RESUME_OPTIONS,
    SCHEDULE,
    HR
)


class City(models.Model):
    """
        Модель города.
    """
    id = models.IntegerField(primary_key=True)
    name = models.CharField(verbose_name='название города', max_length=256)

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'
        ordering = ('name',)

    def __str__(self):
        return self.name


class ProfessionArea(models.Model):
    """
        Модель Профессиональной области.
    """
    name = models.CharField(verbose_name='профессиональная область',
                            max_length=100)

    class Meta:
        verbose_name = 'Профессиональная область'
        verbose_name_plural = 'Профессиональные области'
        ordering = ('prof_area',)

    def __str__(self):
        return self.name


class Duty(models.Model):
    name = models.CharField('Обязанность', max_length=256)

    class Meta:
        verbose_name = 'Обязанность'
        verbose_name_plural = 'Обязанности'
        ordering = ('prof_area',)

    def __str__(self):
        return self.name


class Skill(models.Model):
    name = models.CharField('Навык', max_length=256)

    class Meta:
        verbose_name = 'Навык'
        verbose_name_plural = 'Навыки'
        ordering = ('name',)

    def __str__(self):
        return self.name


class Profession(models.Model):
    """
        Модель профессии.
    """
    id = models.IntegerField(primary_key=True)
    prof_area = models.ForeignKey(ProfessionArea,
                                  verbose_name='профессиональная область',
                                  on_delete=models.CASCADE)
    prof_name = models.CharField(verbose_name='профессия',
                                 max_length=100)
    employeeResponsibilities = models.ManyToManyField(
        Duty, verbose_name='обязанности'
    )
    softwareSkills = models.ManyToManyField(Skill,
                                            verbose_name='Навыки')

    def get_relevant_employeeResponsibilities(self):
        """
            Подбор релевантных обязанностей.
        """
        return Duty.objects.filter(profession__name=self.name)

    def get_relevant_softwareSkills(self):
        """
            Подбор релевантных навыков.
        """
        return Skill.objects.filter(profession__name=self.name)

    class Meta:
        verbose_name = 'Профессия'
        verbose_name_plural = 'Профессии'
        ordering = ('prof_name',)

    def __str__(self):
        return self.prof_name


class Salary(models.Model):
    """
        Модель зарплата.
    """
    salary_min = models.IntegerField(verbose_name='зарплата от')
    salary_max = models.IntegerField(verbose_name='зарплата до')

    def clean(self):
        if self.salary_min and self.salary_max and \
                self.salary_min > self.salary_max:
            raise ValidationError(
                'Зарплата "до" не может быть ниже, чем зарплата "от".'
            )
        super(Salary, self).clean()

    class Meta:
        verbose_name = 'Зарплата'
        verbose_name_plural = 'Зарплаты'
        ordering = ('pk',)

    def __str__(self):
        return f'зарплата от {str(self.salary_min)} до {str(self.salary_max)}'


class Description(models.Model):
    """
        Модель описание вакансии.
    """
    education = models.TextField(verbose_name='образование', choices=EDUCATION)
    experience = models.PositiveSmallIntegerField(verbose_name='стаж')
    citizenship = models.TextField(verbose_name='гражданство', choices=CITIZENSHIP)
    drivingLicense = models.BooleanField(verbose_name='водительские права')
    carOwnership = models.BooleanField(verbose_name='автомобиль')

    class Meta:
        verbose_name = 'Описание вакансии'
        verbose_name_plural = 'Описание вакансий'
        ordering = ('pk',)


class SocialPackage(models.Model):
    """
        Модель социального пакета.
    """
    name = models.CharField(verbose_name='бонус', max_length=256)

    class Meta:
        verbose_name = 'Социальный пакет'
        verbose_name_plural = 'Социальные пакеты'
        ordering = ('prof_name',)

    def __str__(self):
        return self.name


class Conditions(models.Model):
    """
        Модель условия работы.
    """
    workSchedule = models.TextField(verbose_name='График работы',
                                    choices=SCHEDULE)
    workFormat = models.TextField(verbose_name='Формат работы',
                                  choices=EMPLOYMENT_TYPE)
    contractType = models.TextField('verbose_name=Способ оформления',
                                        choices=EMPLOYMENT_METHOD)
    socialPackage = models.ManyToManyField(SocialPackage,
                                            verbose_name='Социальный пакет')
    
    class Meta:
        verbose_name = 'Условия работы'
        verbose_name_plural = 'Условия работы'
        ordering = ('pk',)


# class Partnership(models.Model):
#     """
#         Модель условия сотрудничества.
#     """
#     payment_method = models.TextField(choices=PAYMENT)
#     reward = models.PositiveIntegerField(
#         'Вознаграждение',
#         validators=[MinValueValidator(AMOUNT_MIN_VALUE)]
#     )
#     employment = models.PositiveSmallIntegerField('Количество Сотрудников')
#     resume_date = models.DateField('Дата получения резюме')
#     work_date = models.DateField('Дата выхода на работу')
#     hr_duties = models.ManyToManyField(HRDuty,
#                                        verbose_name='Что входит в'
#                                                     'работу рекрутера')  # ?
#     resume_method = models.TextField('Вид резюме', choices=RESUME_OPTIONS)

#     class Meta:
#         verbose_name = 'Условия сотрудничества'
#         verbose_name_plural = 'Условия сотрудничества'
#         ordering = ('pk',)


# class Recruiter(models.Model):
#     """
#         Модель требование к рекрутерам.
#     """
#     hr_experience = models.PositiveSmallIntegerField('Трудовой стаж рекрутера')
#     hr_skills = models.ManyToManyField(HRSkill,
#                                        verbose_name='Навыки рекрутера')  # ?
#     additional_tasks = models.TextField('Дополнительные задачи')
#     firms_only = models.BooleanField('Только для юрлиц, ИП, самозанятых')
#     black_list = models.TextField('Стоп-лист')
#     hr_number = models.SmallIntegerField('Количество рекрутеров')

#     class Meta:
#         verbose_name = 'Требование к рекрутерам'
#         verbose_name_plural = 'Требования к рекрутерам'
#         ordering = ('pk',)


class Inquery(models.Model):
    """
        Модель заявки.
    """
    name = models.CharField('название', max_length=128)
    prof = models.ForeignKey(Profession, on_delete=models.CASCADE,
                             related_name='prof', verbose_name='профессия')
    city = models.ForeignKey(City, on_delete=models.CASCADE,
                             related_name='city', verbose_name='город')
    salaryRange = models.OneToOneField(Salary, verbose_name='зарплата')
    description = models.OneToOneField(Description,
                                       verbose_name='описание вакансии')
    conditions = models.OneToOneField(Conditions,
                                      verbose_name='условия работы')
    partnership = models.OneToOneField(Partnership,
                                       verbose_name='условия сотрудничества')
    recruiter = models.OneToOneField(Recruiter,
                                     verbose_name='требования к рекрутерам')
    
    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'
        ordering = ('name',)

    def __str__(self):
        return self.name
    

# проверить и подогнать под поля модели Recruiter и Partnership
# посмотреть константы и запросить у коллег что там должно лежать
# поля json которые не разобрал еще 
#                                   |
#                                   |
#                                 \ | /
#                                  \ /
#                                   v

    "employeeReward": 10000000,
    "paymentType": "50% за выход + 50% по окончании гарантийного периода (1-3 мес.)",
    "employeeCount": 5,
    "recruiterTasks": [
        "Организация собеседований с заказчиком, синхронизация по времени соискателя и заказчика"
    ],
    "resumeFormat": "Резюме кандидатов, с которыми проведено интервью (с комментариями)",
    "dates": {
        "desiredFirstResumeDate": 1710720000000,
        "desiredEmployeeExitDate": 1711497600000
    },
    "experienceYears": 4,
    "specialSkills": [
        "Проведение собеседований",
        "Работа с HR-платформами",
        "Оценка компетенций"
    ],
    "additionalTasks": [
        "Организация тренингов и семинаров для повышения квалификации персонала",
        "Ведение отчетности по итогам подбора персонала",
        "Анализ эффективности каналов поиска кандидатов"
    ],
    "isIndividual": true,
    "blacklistedCompanies": [],
    "recruiterCount": 1,
    "acceptOffer": true

