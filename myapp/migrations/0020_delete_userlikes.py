# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0019_remove_vehicles_like_count'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Userlikes',
        ),
    ]
