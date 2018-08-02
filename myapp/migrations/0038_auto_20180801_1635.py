# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0037_auto_20180801_1629'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userlikes',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
