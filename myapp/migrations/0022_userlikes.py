# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0021_vehicles_like_count'),
    ]

    operations = [
        migrations.CreateModel(
            name='Userlikes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('company_id', models.IntegerField(null=True, blank=True)),
                ('user_id', models.IntegerField(null=True, blank=True)),
                ('vehicle_id', models.IntegerField(null=True, blank=True)),
            ],
        ),
    ]
