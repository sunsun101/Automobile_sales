# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0039_userlikes_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicles',
            name='condition',
            field=models.CharField(max_length=10, null=True, blank=True),
        ),
    ]
