# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-20 22:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0011_teacher_has_favor'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='favor_id',
            field=models.IntegerField(default=0, verbose_name='收藏用户'),
        ),
    ]