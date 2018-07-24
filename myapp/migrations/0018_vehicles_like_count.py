# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0017_auto_20180716_0305'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicles',
            name='like_count',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
