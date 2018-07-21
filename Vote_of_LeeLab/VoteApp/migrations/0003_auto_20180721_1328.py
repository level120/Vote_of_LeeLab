# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-07-21 04:28
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('VoteApp', '0002_auto_20180720_1605'),
    ]

    operations = [
        migrations.AddField(
            model_name='like',
            name='slug',
            field=models.SlugField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='like',
            name='likes',
            field=models.ManyToManyField(related_name='likes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='like',
            name='prize',
            field=models.BooleanField(db_column='우승이력', default=False),
        ),
    ]
