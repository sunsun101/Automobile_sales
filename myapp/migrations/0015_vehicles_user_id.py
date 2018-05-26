# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0014_auto_20180526_1304'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicles',
            name='user_id',
            field=models.ForeignKey(blank=True, to='myapp.Userprofile', null=True),
        ),
    ]
