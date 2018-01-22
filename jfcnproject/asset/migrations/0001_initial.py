# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-18 16:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AssetManagement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=15)),
                ('host_name', models.CharField(max_length=255, verbose_name='主机名')),
                ('project', models.CharField(max_length=255, verbose_name='所属项目')),
                ('system', models.CharField(max_length=20, verbose_name='操作系统')),
                ('cpu', models.CharField(max_length=20)),
                ('memory', models.CharField(max_length=20, verbose_name='内存')),
                ('hard', models.CharField(max_length=20, verbose_name='硬盘')),
                ('remark', models.CharField(blank=True, max_length=255, null=True, verbose_name='备注')),
            ],
        ),
    ]