# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0029_auto_20180729_1707'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userlikes',
            name='month',
            field=models.IntegerField(null=True),
        ),
    ]
