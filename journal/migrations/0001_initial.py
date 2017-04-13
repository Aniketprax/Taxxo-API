# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-04-13 12:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Journal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('credit_amount', models.IntegerField()),
                ('debit_amount', models.IntegerField()),
                ('narration', models.CharField(max_length=1000)),
                ('credit_account', models.CharField(max_length=1000)),
                ('debit_account', models.CharField(max_length=1000)),
            ],
        ),
    ]
