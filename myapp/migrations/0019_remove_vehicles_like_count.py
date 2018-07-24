# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0018_vehicles_like_count'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vehicles',
            name='like_count',
        ),
    ]
