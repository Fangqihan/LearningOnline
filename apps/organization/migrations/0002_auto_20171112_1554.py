# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-12 15:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='name',
            field=models.CharField(max_length=50, verbose_name='城市名称'),
        ),
    ]