# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-09 09:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='start',
            name='kakao',
            field=models.CharField(max_length=100),
        ),
    ]
