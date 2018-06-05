# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-20 20:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0007_auto_20171119_1015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='chapter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.Chapter', verbose_name='所属章节'),
        ),
    ]
