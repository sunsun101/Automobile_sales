# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myapp', '0002_auto_20180304_0502'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=20, blank=True)),
                ('birth_date', models.DateField(null=True, blank=True)),
                ('gender', models.CharField(max_length=10)),
                ('username', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
