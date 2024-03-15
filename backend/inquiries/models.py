from django.db import models
from django.forms import ValidationError


# Condition


PAYMENT_CHOICES = (
    ('100%', '100% сразу'),
    ('50-50', '50% сразу и 50% после'),
    ('100-after', '100% после')
)


class Condition(models.Model):
    """
    Модель условия сотрудничества.
    """
    payment = models.TextField(verbose_name='условия оплаты',
                               choices=PAYMENT_CHOICES)


# Vacancy


class City(models.Model):
    """
    Модель города.
    """
    name = models.CharField(verbose_name='города', max_length=256)

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'
        ordering = ('name',)

    def __str__(self):
        return self.name


class Location(models.Model):
    """
    Модель расположения.
    """
    name = models.CharField(verbose_name='название региона', max_length=256)
    cities = models.ManyToManyField(City, verbose_name='города')

    class Meta:
        verbose_name = 'Регион'
        verbose_name_plural = 'Регионы'
        ordering = ('name',)

    def __str__(self):
        return self.name


class Profession(models.Model):
    """
    Модель профессии.
    """
    name = models.CharField(verbose_name='профессия', max_length=256)

    class Meta:
        verbose_name = 'Профессия'
        verbose_name_plural = 'Профессии'
        ordering = ('name',)

    def __str__(self):
        return self.name


class Position(models.Model):
    """
    Модель позиции.
    """
    name = models.CharField(verbose_name='название области применения',
                            max_length=256)
    professions = models.ManyToManyField(Profession, verbose_name='профессии')

    class Meta:
        verbose_name = 'Область'
        verbose_name_plural = 'Области'
        ordering = ('name',)

    def __str__(self):
        return self.name


class Vacancy(models.Model):
    """
    Модель вакансии.
    """
    name = models.CharField(verbose_name='название', max_length=100)
    location = models.ForeignKey(Location,
                                 verbose_name='город',
                                 on_delete=models.CASCADE)
    position = models.ForeignKey(Position,
                                 verbose_name='профессия',
                                 on_delete=models.CASCADE)
    description = models.TextField(verbose_name='описание')
    salary_low = models.DecimalField(verbose_name='зарплата от',
                                     max_digits=10, decimal_places=2)
    salary_high = models.DecimalField(verbose_name='зарплата до',
                                      max_digits=10, decimal_places=2)
    condition = models.OneToOneField(Condition, on_delete=models.CASCADE)

    def clean(self):
        if self.salary_low and self.salary_high and self.salary_low > self.salary_high:
            raise ValidationError(
                'Зарплата "до" не может быть ниже, чем зарплата "от".'
            )
        super(Vacancy, self).clean()

    class Meta:
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансии'
        ordering = ('name',)

    def __str__(self):
        return self.name
