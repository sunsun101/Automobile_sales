# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0036_auto_20180801_1523'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userlikes',
            name='date',
            field=models.DateTimeField(null=True, blank=True),
        ),
    ]
