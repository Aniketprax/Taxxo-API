# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-04-08 17:05
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0009_auto_20170408_2234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='admin',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
