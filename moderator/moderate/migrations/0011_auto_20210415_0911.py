# Generated by Django 3.2 on 2021-04-15 09:11

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('moderate', '0010_event_created_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='mozillianprofile',
            name='avatar_url',
            field=models.URLField(blank=True, default='', max_length=400),
        ),
        migrations.AlterField(
            model_name='question',
            name='answer',
            field=models.TextField(blank=True, default='', validators=[django.core.validators.MaxLengthValidator(280)]),
        ),
        migrations.AlterField(
            model_name='question',
            name='asked_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
