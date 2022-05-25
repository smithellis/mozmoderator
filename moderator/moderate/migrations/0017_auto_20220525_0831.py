# Generated by Django 3.1.14 on 2022-05-25 08:31

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moderate', '0016_auto_20220426_1213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='answer',
            field=models.TextField(blank=True, default='', validators=[django.core.validators.MaxLengthValidator(2500)]),
        ),
    ]
