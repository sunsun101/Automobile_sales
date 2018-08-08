# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0038_auto_20180801_1635'),
    ]

    operations = [
        migrations.AddField(
            model_name='userlikes',
            name='rating',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
