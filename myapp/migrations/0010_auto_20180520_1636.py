# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_auto_20180518_0554'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='user',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='password',
            field=models.CharField(max_length=16, blank=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='user_name',
            field=models.CharField(max_length=30, blank=True),
        ),
    ]
