# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0023_userprofile_company_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userlikes',
            old_name='user_id',
            new_name='liker_id',
        ),
    ]
