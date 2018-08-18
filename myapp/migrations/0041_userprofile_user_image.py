# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0040_vehicles_condition'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='user_image',
            field=models.ImageField(upload_to=b'user_image', blank=True),
        ),
    ]
