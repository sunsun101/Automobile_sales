# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0015_vehicles_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicles',
            name='user_id',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
