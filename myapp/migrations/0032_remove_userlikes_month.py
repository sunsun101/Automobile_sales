# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0031_auto_20180729_1713'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userlikes',
            name='month',
        ),
    ]
