# Generated by Django 5.0.2 on 2024-03-20 12:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inquiries', '0004_alter_inquiry_softwareskills'),
    ]

    operations = [
        migrations.AlterField(
            model_name='duty',
            name='profession',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='duties', to='inquiries.professionarea', verbose_name='профессия'),
        ),
        migrations.AlterField(
            model_name='skill',
            name='profession',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='skills', to='inquiries.professionarea', verbose_name='профессия'),
        ),
    ]
