# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0035_auto_20180801_1438'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userlikes',
            old_name='month',
            new_name='date',
        ),
    ]
