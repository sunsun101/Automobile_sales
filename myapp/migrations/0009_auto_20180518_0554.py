# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myapp', '0008_vehicles'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='password',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='user_name',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='user',
            field=models.OneToOneField(null=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
