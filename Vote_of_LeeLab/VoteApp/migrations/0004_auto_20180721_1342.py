# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-07-21 04:42
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('VoteApp', '0003_auto_20180721_1328'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='like',
            name='slug',
        ),
        migrations.AlterField(
            model_name='like',
            name='likes',
            field=models.ManyToManyField(blank=True, null=True, related_name='likes', to=settings.AUTH_USER_MODEL),
        ),
    ]
