# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0013_remove_userprofile_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicles',
            name='brand',
            field=models.CharField(max_length=20, blank=True),
        ),
        migrations.AddField(
            model_name='vehicles',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='vehicles',
            name='engine_power',
            field=models.CharField(max_length=20, blank=True),
        ),
        migrations.AddField(
            model_name='vehicles',
            name='model_no',
            field=models.CharField(max_length=50, blank=True),
        ),
        migrations.AddField(
            model_name='vehicles',
            name='price',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='vehicles',
            name='vehicle_type',
            field=models.CharField(max_length=20, blank=True),
        ),
    ]
