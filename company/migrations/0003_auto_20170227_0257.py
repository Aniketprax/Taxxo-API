# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-02-26 21:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0002_auto_20170227_0256'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Comany',
            new_name='Company',
        ),
    ]