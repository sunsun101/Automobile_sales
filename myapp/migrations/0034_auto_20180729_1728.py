# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0033_userlikes_month'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userlikes',
            name='month',
            field=models.IntegerField(default=7, null=True),
        ),
    ]
