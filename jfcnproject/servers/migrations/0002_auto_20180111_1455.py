# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-11 14:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appmanagement',
            name='code_state',
            field=models.CharField(choices=[('2', 'start'), ('3', 'stop'), ('4', 'restart'), ('1', 'None')], default='1', max_length=10, verbose_name='操作动作'),
        ),
    ]