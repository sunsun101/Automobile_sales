# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0024_auto_20180722_1226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='Acc_type',
            field=models.CharField(default=b'I', max_length=10),
        ),
    ]
