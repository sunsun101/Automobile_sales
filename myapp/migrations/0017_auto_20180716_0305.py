# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0016_auto_20180526_1804'),
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
        migrations.AlterField(
            model_name='userprofile',
            name='email',
            field=models.CharField(max_length=100, unique=True, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user_name',
            field=models.CharField(unique=True, max_length=30, blank=True),
        ),
    ]
