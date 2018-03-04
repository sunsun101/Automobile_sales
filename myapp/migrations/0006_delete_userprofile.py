# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_auto_20180304_0901'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Userprofile',
        ),
    ]
