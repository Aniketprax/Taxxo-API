# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-02-28 16:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('company', '0005_auto_20170228_2136'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ledgers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
                ('groups', models.CharField(choices=[('bank OCC AC', 'bank OCC AC'), ('bank OD AC', 'bank OD AC'), ('branch Division', 'branch Division'), ('capital AC', 'capital AC'), ('cash in hand', 'cash in hand'), ('current assets', 'current assets'), ('current liabilities', 'current liabilities'), ('deposits assets', 'deposits assets'), ('direct expenses', 'direct expenses'), ('direct income', 'direct income'), ('duties n taxes', 'duties n taxes'), ('expenses direct', 'expenses direct'), ('expenses indirect', 'expenses indirect'), ('fixed assets', 'fixed assets'), ('income direct', 'income direct'), ('income indirect', 'income indirect'), ('indirect expenses', 'indirect expenses'), ('indirect income', 'indirect income'), ('investments', 'investments'), ('loans n advances assets', 'loans n advances assets'), ('loan liability', 'loan liability'), ('misc exoenses', 'misc exoenses'), ('provisions', 'provisions'), ('purchase AC', 'purchase AC'), ('reserve n surpulus', 'reserve n surplus'), ('retaines earnings', 'retaines earnings'), ('sales accounts', 'sales accounts'), ('secured loans', 'secured loans'), ('stock in hand', 'stock in hand'), ('sundry creditors', 'sundry creditors'), ('sundry debitors', 'sundry debitors'), ('suspense Account', 'suspense Account'), ('unsecured loans', 'unsecured loans')], max_length=1000)),
                ('opening_balance', models.IntegerField(default=0)),
                ('type', models.CharField(choices=[('Accounts', 'Accounts'), ('Inventory', 'Inventory')], max_length=1000)),
                ('inventory', models.BooleanField(default=False)),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.Company')),
            ],
        ),
    ]