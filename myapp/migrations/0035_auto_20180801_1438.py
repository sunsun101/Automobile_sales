# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0034_auto_20180729_1728'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userlikes',
            name='month',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
