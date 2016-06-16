# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-06-16 10:30
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Start',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('style1', models.BooleanField(default=False)),
                ('style2', models.BooleanField(default=False)),
                ('style3', models.BooleanField(default=False)),
                ('style4', models.BooleanField(default=False)),
                ('size_top', models.CharField(choices=[('S', 'S'), ('M', 'M'), ('L', 'L'), ('XL', 'XL'), ('XXL', 'XXL'), ('XXXL', 'XXXL')], default='M', max_length=6)),
                ('size_bottom', models.CharField(choices=[('S', 'S'), ('M', 'M'), ('L', 'L'), ('XL', 'XL'), ('XXL', 'XXL'), ('XXXL', 'XXXL')], default='M', max_length=6)),
                ('kakao', models.CharField(max_length=100)),
                ('address', models.TextField()),
                ('name', models.CharField(default='', max_length=100, null=True)),
                ('created_date', models.DateTimeField(default=datetime.datetime(2016, 6, 16, 10, 30, 9, 239172))),
                ('expiration_date', models.DateTimeField(default=datetime.datetime(2016, 7, 16, 10, 30, 9, 239219))),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='start', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
