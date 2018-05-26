# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_auto_20180520_1636'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='Acc_type',
            field=models.CharField(default=b'individual', max_length=10),
        ),
    ]
