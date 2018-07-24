# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0022_userlikes'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='company_name',
            field=models.CharField(max_length=50, blank=True),
        ),
    ]
