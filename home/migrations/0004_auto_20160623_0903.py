# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-06-23 09:03
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20160623_0902'),
    ]

    operations = [
        migrations.AlterField(
            model_name='start',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 6, 23, 9, 3, 23, 438986)),
        ),
        migrations.AlterField(
            model_name='start',
            name='expiration_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 7, 23, 9, 3, 23, 439018)),
        ),
    ]
