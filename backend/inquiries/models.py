from django.db import models
from django.forms import ValidationError
from django.utils import timezone
from django.core.validators import MinValueValidator

from .constants import (
    CITIZENSHIP,
    EDUCATION,
    EMPLOYMENT_TYPE,
    EMPLOYMENT_METHOD,
    MIN_EMPLOYEE_REWARD,
    PAYMENT,
    RESUME_OPTIONS,
    SCHEDULE,
)


class City(models.Model):
    """
        Модель города.
    """
    id = models.IntegerField(
        primary_key=True
    )

    name = models.CharField(
        verbose_name='название города',
        max_length=256
    )

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'
        ordering = ('name',)

    def __str__(self):
        return self.name


class ProfessionArea(models.Model):
    """
        Модель профессиональной области.
    """
    name = models.CharField(
        verbose_name='профессиональная область',
        max_length=256
    )

    class Meta:
        verbose_name = 'Профессиональная область'
        verbose_name_plural = 'Профессиональные области'
        ordering = ('name',)

    def __str__(self):
        return self.name


class Duty(models.Model):
    """
        Модель обязанности.
    """
    name = models.CharField(
        verbose_name='обязанность',
        max_length=256
    )

    prof_area = models.ForeignKey(
        ProfessionArea,
        on_delete=models.CASCADE,
        related_name='duty_prof_area',
        verbose_name='проф область'
    )

    class Meta:
        verbose_name = 'Обязанность'
        verbose_name_plural = 'Обязанности'
        ordering = ('name',)

    def __str__(self):
        return self.name


class Software(models.Model):
    """
        Модель программы.
    """
    name = models.CharField(
        verbose_name='программа',
        max_length=256
    )

    class Meta:
        verbose_name = 'Программа'
        verbose_name_plural = 'Программы'
        ordering = ('name',)

    def __str__(self):
        return self.name


class Profession(models.Model):
    """
        Модель профессии.
    """
    id = models.IntegerField(
        primary_key=True
    )

    prof_area = models.ForeignKey(
        ProfessionArea,
        related_name='prof_area',
        verbose_name='профессиональная область',
        on_delete=models.CASCADE
    )

    prof_name = models.CharField(
        verbose_name='профессия',
        max_length=256
    )

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
    education = models.TextField(
        verbose_name='образование',
        choices=EDUCATION
    )

    experience = models.PositiveSmallIntegerField(
        verbose_name='стаж'
    )

    citizenship = models.TextField(
        verbose_name='гражданство',
        choices=CITIZENSHIP
    )

    drivingLicense = models.BooleanField(
        verbose_name='водительские права'
    )

    carOwnership = models.BooleanField(
        verbose_name='автомобиль'
    )

    class Meta:
        verbose_name = 'Описание вакансии'
        verbose_name_plural = 'Описание вакансий'
        ordering = ('pk',)


class SocialPackage(models.Model):
    """
        Модель социального пакета.
    """
    name = models.CharField(
        verbose_name='социальный пакет',
        max_length=256
    )

    class Meta:
        verbose_name = 'Социальный пакет'
        verbose_name_plural = 'Социальные пакеты'
        ordering = ('name',)

    def __str__(self):
        return self.name


class Conditions(models.Model):
    """
        Модель условия работы.
    """
    workSchedule = models.TextField(
        verbose_name='график работы',
        choices=SCHEDULE
    )

    workFormat = models.TextField(
        verbose_name='формат работы',
        choices=EMPLOYMENT_TYPE
    )

    contractType = models.TextField(
        verbose_name='способ оформления',
        choices=EMPLOYMENT_METHOD
    )

    socialPackage = models.ManyToManyField(
        SocialPackage,
        related_name='social_package',
        verbose_name='социальный пакет'
    )

    class Meta:
        verbose_name = 'Условия работы'
        verbose_name_plural = 'Условия работы'
        ordering = ('pk',)


class TaskRecruiter(models.Model):
    """
        Модель задачи рекрутера.
    """
    name = models.CharField(
        verbose_name='задача',
        max_length=256
    )

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
        ordering = ('name',)

    def __str__(self):
        return self.name


class Partnership(models.Model):
    """
        Модель условия сотрудничества.
    """
    employeeReward = models.PositiveIntegerField(
        verbose_name='вознаграждение',
        validators=[MinValueValidator(MIN_EMPLOYEE_REWARD)],
    )

    paymentType = models.TextField(
        verbose_name='тип оплаты',
        choices=PAYMENT,
    )

    employeeCount = models.PositiveSmallIntegerField(
        verbose_name='количество сотрудников',
    )

    recruiterTasks = models.ManyToManyField(
        TaskRecruiter,
        related_name='task_recruiter',
        verbose_name='задачи рекрутера',
    )

    desiredFirstResumeDate = models.DateField(
        verbose_name='дата получения резюме',
    )

    desiredEmployeeExitDate = models.DateField(
        verbose_name='дата выхода на работу',
    )

    resumeFormat = models.TextField(
        verbose_name='вид резюме',
        choices=RESUME_OPTIONS,
    )

    class Meta:
        verbose_name = 'Условия сотрудничества'
        verbose_name_plural = 'Условия сотрудничества'
        ordering = ('pk',)

    def clean(self):
        if self.desiredEmployeeExitDate < timezone.now().date():
            raise ValidationError(
                'Дата выхода на работу не может быть раньше сегодняшней даты.'
            )

        if self.desiredEmployeeExitDate < self.desiredFirstResumeDate:
            raise ValidationError(
                'Дата выхода на работу должна быть позже даты получения резюме'
            )


class Company(models.Model):
    """
        Модель компании.
    """
    name = models.CharField(
        verbose_name='компания',
        max_length=256
    )

    class Meta:
        verbose_name = 'Компания'
        verbose_name_plural = 'Компании'
        ordering = ('name',)

    def __str__(self):
        return self.name


class TaskAdditional(models.Model):
    """
        Модель дополнительные задачи.
    """
    name = models.CharField(
        verbose_name='дополнительная задача',
        max_length=256
    )

    class Meta:
        verbose_name = 'Дополнительная задача'
        verbose_name_plural = 'Дополнительные задачи'
        ordering = ('name',)

    def __str__(self):
        return self.name


class SkillRecruiter(models.Model):
    """
        Модель навыки рекрутера.
    """
    name = models.CharField(
        verbose_name='навык',
        max_length=256
    )

    class Meta:
        verbose_name = 'Навык рекрутера'
        verbose_name_plural = 'Навыки рекрутера'
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

    specialSkills = models.ManyToManyField(
        SkillRecruiter,
        related_name='skill_recruiter',
        verbose_name='навыки рекрутера'
    )

    additionalTasks = models.ManyToManyField(
        TaskAdditional,
        related_name='task_additional',
        verbose_name='задачи рекрутера'
    )

    isIndividual = models.BooleanField(
        verbose_name='юрлица, ИП, самозанятые'
    )

    blacklistedCompanies = models.ManyToManyField(
        Company,
        related_name='company',
        verbose_name='стоп лист'
    )

    recruiterCount = models.SmallIntegerField(
        verbose_name='число рекрутеров'
    )

    class Meta:
        verbose_name = 'Требование к рекрутерам'
        verbose_name_plural = 'Требования к рекрутерам'
        ordering = ('pk',)


class Inquiry(models.Model):
    """
        Модель заявки.
    """
    name = models.CharField(
        verbose_name='название',
        max_length=128
    )

    prof = models.ForeignKey(
        Profession,
        on_delete=models.CASCADE,
        related_name='prof',
        verbose_name='профессия'
    )

    employeeResponsibilities = models.ManyToManyField(
        Duty,
        related_name='duty',
        verbose_name='обязанности'
    )

    softwareSkills = models.ManyToManyField(
        Software,
        related_name='skill_software',
        verbose_name='знание программ',
        blank=True
    )

    city = models.ForeignKey(
        City,
        on_delete=models.CASCADE,
        related_name='city',
        verbose_name='город'
    )

    salary_min = models.IntegerField(
        verbose_name='зарплата от'
    )

    salary_max = models.IntegerField(
        verbose_name='зарплата до'
    )

    description = models.OneToOneField(
        Description,
        related_name='description',
        on_delete=models.CASCADE,
        verbose_name='описание вакансии'
    )

    conditions = models.OneToOneField(
        Conditions,
        related_name='conditions',
        on_delete=models.CASCADE,
        verbose_name='условия работы'
    )

    partnership = models.OneToOneField(
        Partnership,
        related_name='partnership',
        on_delete=models.CASCADE,
        verbose_name='условия сотрудничества'
    )

    recruiter = models.OneToOneField(
        Recruiter,
        related_name='recruiter',
        on_delete=models.CASCADE,
        verbose_name='требования к рекрутерам'
    )

    def get_relevant_employeeResponsibilities(self):
        """
            Подбор релевантных обязанностей.
        """
        return self.prof.duties.all()

    def clean(self):
        if self.salary_min and self.salary_max and \
                self.salary_min > self.salary_max:
            raise ValidationError(
                'Зарплата "до" не может быть ниже, чем зарплата "от".'
            )
        super(Inquiry, self).clean()

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'
        ordering = ('name',)

    def __str__(self):
        return self.name
