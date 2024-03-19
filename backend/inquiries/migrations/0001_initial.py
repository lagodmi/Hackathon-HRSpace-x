# Generated by Django 5.0.2 on 2024-03-19 07:37

import django.core.validators
import django.db.models.deletion
import inquiries.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=256, verbose_name='название города')),
            ],
            options={
                'verbose_name': 'Город',
                'verbose_name_plural': 'Города',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='компания')),
            ],
            options={
                'verbose_name': 'Компания',
                'verbose_name_plural': 'Компании',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Conditions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('workSchedule', models.TextField(choices=[('1', 'Пятидневная неделя'), ('2', 'Сменная работа'), ('3', 'Вахтовый метод')], verbose_name='График работы')),
                ('workFormat', models.TextField(choices=[('1', 'Полный день'), ('2', 'Гибкий график'), ('3', 'Удаленная работа')], verbose_name='Формат работы')),
                ('contractType', models.TextField(choices=[('1', 'Трудовой договор'), ('2', 'Договор ГПХ с физ.лицом'), ('3', 'Договор ГПХ с ИП и самозанятым')], verbose_name='verbose_name=Способ оформления')),
            ],
            options={
                'verbose_name': 'Условия работы',
                'verbose_name_plural': 'Условия работы',
                'ordering': ('pk',),
            },
        ),
        migrations.CreateModel(
            name='Description',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('education', models.TextField(choices=[('1', 'Высшее'), ('2', 'Неоконченное высшее'), ('3', 'Среднее-специальное'), ('4', 'Любое')], verbose_name='образование')),
                ('experience', models.PositiveSmallIntegerField(verbose_name='стаж')),
                ('citizenship', models.TextField(choices=[('1', 'РФ'), ('2', 'Любое')], verbose_name='гражданство')),
                ('drivingLicense', models.BooleanField(verbose_name='водительские права')),
                ('carOwnership', models.BooleanField(verbose_name='автомобиль')),
            ],
            options={
                'verbose_name': 'Описание вакансии',
                'verbose_name_plural': 'Описание вакансий',
                'ordering': ('pk',),
            },
        ),
        migrations.CreateModel(
            name='Duty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Обязанность')),
            ],
            options={
                'verbose_name': 'Обязанность',
                'verbose_name_plural': 'Обязанности',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Partnership',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employeeReward', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(10000)], verbose_name='вознаграждение')),
                ('paymentType', models.TextField(choices=[('1', '100% за выход'), ('2', '50/50'), ('3', '100% после испытательного срока')], verbose_name='тип оплаты')),
                ('employeeCount', models.PositiveSmallIntegerField(verbose_name='количество сотрудников')),
                ('desiredFirstResumeDate', models.DateField(validators=[inquiries.validators.validate_desiredFirstResumeDate_date], verbose_name='дата получения резюме')),
                ('desiredEmployeeExitDate', models.DateField(validators=[inquiries.validators.validate_desiredEmployeeExitDate_date], verbose_name='дата выхода на работу')),
                ('resumeFormat', models.TextField(choices=[('1', 'без собеседования'), ('2', 'с интервью')], verbose_name='Вид резюме')),
            ],
            options={
                'verbose_name': 'Условия сотрудничества',
                'verbose_name_plural': 'Условия сотрудничества',
                'ordering': ('pk',),
            },
        ),
        migrations.CreateModel(
            name='ProfessionArea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='профессиональная область')),
            ],
            options={
                'verbose_name': 'Профессиональная область',
                'verbose_name_plural': 'Профессиональные области',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Навык')),
            ],
            options={
                'verbose_name': 'Навык',
                'verbose_name_plural': 'Навыки',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='SkillRecruiter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='навык')),
            ],
            options={
                'verbose_name': 'Навык рекрутера',
                'verbose_name_plural': 'навыки рекрутера',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='SocialPackage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='социальный пакет')),
            ],
            options={
                'verbose_name': 'Социальный пакет',
                'verbose_name_plural': 'Социальные пакеты',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='TaskAdditional',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='дополнительная задача')),
            ],
            options={
                'verbose_name': 'Дополнительная задача',
                'verbose_name_plural': 'Дополнительные задачи',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='TaskRecruiter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='задача')),
            ],
            options={
                'verbose_name': 'Задача',
                'verbose_name_plural': 'Задачи',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Profession',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('prof_name', models.CharField(max_length=256, verbose_name='профессия')),
                ('employeeResponsibilities', models.ManyToManyField(related_name='duty', to='inquiries.duty', verbose_name='обязанности')),
                ('prof_area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inquiries.professionarea', verbose_name='профессиональная область')),
                ('softwareSkills', models.ManyToManyField(related_name='skill_software', to='inquiries.skill', verbose_name='Навыки')),
            ],
            options={
                'verbose_name': 'Профессия',
                'verbose_name_plural': 'Профессии',
                'ordering': ('prof_name',),
            },
        ),
        migrations.CreateModel(
            name='Recruiter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('experienceYears', models.PositiveSmallIntegerField(verbose_name='трудовой стаж рекрутера')),
                ('isIndividual', models.BooleanField(verbose_name='юрлица, ИП, самозанятые')),
                ('recruiterCount', models.SmallIntegerField(verbose_name='число рекрутеров')),
                ('blacklistedCompanies', models.ManyToManyField(related_name='company', to='inquiries.company', verbose_name='стоп лист')),
                ('specialSkills', models.ManyToManyField(related_name='skill_recruiter', to='inquiries.skillrecruiter', verbose_name='навыки рекрутера')),
                ('additionalTasks', models.ManyToManyField(related_name='task_additional', to='inquiries.taskadditional', verbose_name='задачи рекрутера')),
            ],
            options={
                'verbose_name': 'Требование к рекрутерам',
                'verbose_name_plural': 'Требования к рекрутерам',
                'ordering': ('pk',),
            },
        ),
        migrations.CreateModel(
            name='Inquery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='название')),
                ('salary_min', models.IntegerField(verbose_name='зарплата от')),
                ('salary_max', models.IntegerField(verbose_name='зарплата до')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='city', to='inquiries.city', verbose_name='город')),
                ('conditions', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='inquiries.conditions', verbose_name='условия работы')),
                ('description', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='inquiries.description', verbose_name='описание вакансии')),
                ('partnership', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='inquiries.partnership', verbose_name='условия сотрудничества')),
                ('prof', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prof', to='inquiries.profession', verbose_name='профессия')),
                ('recruiter', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='inquiries.recruiter', verbose_name='требования к рекрутерам')),
            ],
            options={
                'verbose_name': 'Заявка',
                'verbose_name_plural': 'Заявки',
                'ordering': ('name',),
            },
        ),
        migrations.AddField(
            model_name='conditions',
            name='socialPackage',
            field=models.ManyToManyField(related_name='social_package', to='inquiries.socialpackage', verbose_name='Социальный пакет'),
        ),
        migrations.AddField(
            model_name='partnership',
            name='recruiterTasks',
            field=models.ManyToManyField(related_name='task_recruiter', to='inquiries.taskrecruiter', verbose_name='задачи рекрутера'),
        ),
    ]
