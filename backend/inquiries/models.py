from django.db import models
from django.forms import ValidationError
from django.core.validators import MinValueValidator

from .constants import (
    ADDITIONAL_TASKS,
    CITIZENSHIP,
    EDUCATION,
    EMPLOYMENT_TYPE,
    EMPLOYMENT_METHOD,
    MIN_EMPLOYEE_REWARD,
    PAYMENT,
    RESUME_OPTIONS,
    SCHEDULE,
    SKILLS_SPECIAL,
    TASKS_RECRUITER
)
from .validators import (
    validate_desiredEmployeeExitDate_date,
    validate_desiredFirstResumeDate_date
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
    """
        Модель навыка.
    """
    name = models.CharField(verbose_name='Навык', max_length=256)

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


class Description(models.Model):
    """
        Модель описание вакансии.
    """
    education = models.TextField(verbose_name='образование', choices=EDUCATION)
    experience = models.PositiveSmallIntegerField(verbose_name='стаж')
    citizenship = models.TextField(verbose_name='гражданство',
                                   choices=CITIZENSHIP)
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


class Partnership(models.Model):
    """
        Модель условия сотрудничества.
    """
    employeeReward = models.PositiveIntegerField(
        'Вознаграждение',
        validators=(MinValueValidator(MIN_EMPLOYEE_REWARD),)
    )
    paymentType = models.TextField(choices=PAYMENT)
    employeeCount = models.PositiveSmallIntegerField(
        verbose_name='количество сотрудников'
    )
    recruiterTasks = models.TextField(verbose_name='задачи рекрутера',
                                      choices=TASKS_RECRUITER)
    desiredFirstResumeDate = models.DateField(
        verbose_name='дата получения резюме',
        validators=(validate_desiredFirstResumeDate_date,)
    )
    desiredEmployeeExitDate = models.DateField(
        verbose_name='дата выхода на работу',
        validators=(validate_desiredEmployeeExitDate_date,)
    )
    resumeFormat = models.TextField(verbose_name='Вид резюме',
                                    choices=RESUME_OPTIONS)

    class Meta:
        verbose_name = 'Условия сотрудничества'
        verbose_name_plural = 'Условия сотрудничества'
        ordering = ('pk',)


class Company(models.Model):
    """
        Модель компании.
    """
    name = models.CharField(verbose_name='компания', max_length=256)

    class Meta:
        verbose_name = 'Компания'
        verbose_name_plural = 'Компании'
        ordering = ('name',)

    def __str__(self):
        return self.name


class Recruiter(models.Model):
    """
        Модель требование к рекрутерам.
    """
    experienceYears = models.PositiveSmallIntegerField(
        verbose_name='трудовой стаж рекрутера'
    )
    specialSkills = models.TextField(verbose_name='навыки рекрутера',
                                     choices=SKILLS_SPECIAL)
    additionalTasks = models.TextField(verbose_name='дополнительные задачи',
                                       choices=ADDITIONAL_TASKS)
    isIndividual = models.BooleanField(verbose_name='юрлица, ИП, самозанятые')
    blacklistedCompanies = models.ManyToManyField(
        Company, verbose_name='стоп лист компаний'
    )
    recruiterCount = models.SmallIntegerField(
        verbose_name='количество рекрутеров'
    )

    class Meta:
        verbose_name = 'Требование к рекрутерам'
        verbose_name_plural = 'Требования к рекрутерам'
        ordering = ('pk',)


class Inquery(models.Model):
    """
        Модель заявки.
    """
    name = models.CharField('название', max_length=128)
    prof = models.ForeignKey(Profession, on_delete=models.CASCADE,
                             related_name='prof', verbose_name='профессия')
    city = models.ForeignKey(City, on_delete=models.CASCADE,
                             related_name='city', verbose_name='город')
    salary_min = models.IntegerField(verbose_name='зарплата от')
    salary_max = models.IntegerField(verbose_name='зарплата до')
    description = models.OneToOneField(Description,
                                       verbose_name='описание вакансии')
    conditions = models.OneToOneField(Conditions,
                                      verbose_name='условия работы')
    partnership = models.OneToOneField(Partnership,
                                       verbose_name='условия сотрудничества')
    recruiter = models.OneToOneField(Recruiter,
                                     verbose_name='требования к рекрутерам')

    def clean(self):
        if self.salary_min and self.salary_max and \
                self.salary_min > self.salary_max:
            raise ValidationError(
                'Зарплата "до" не может быть ниже, чем зарплата "от".'
            )
        super(Inquery, self).clean()

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'
        ordering = ('name',)

    def __str__(self):
        return self.name
