# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_auto_20180304_0854'),
    ]

    operations = [
        migrations.CreateModel(
            name='Userprofile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_name', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('first_name', models.CharField(max_length=50, blank=True)),
                ('middle_name', models.CharField(max_length=50, blank=True)),
                ('last_name', models.CharField(max_length=50, blank=True)),
                ('gender', models.CharField(max_length=10, blank=True)),
                ('email', models.CharField(max_length=100, null=True)),
                ('birth_date', models.DateField(null=True, blank=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
