# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-08-03 14:26
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('VoteApp', '0008_auto_20180722_1856'),
    ]

    operations = [
        migrations.AlterField(
            model_name='votedate',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 8, 10, 14, 26, 44, 790632)),
        ),
        migrations.AlterField(
            model_name='votedate',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 8, 3, 14, 26, 45, 790632)),
        ),
    ]
