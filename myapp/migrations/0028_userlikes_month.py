# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0027_auto_20180724_0452'),
    ]

    operations = [
        migrations.AddField(
            model_name='userlikes',
            name='month',
            field=models.DateField(null=True),
        ),
    ]
