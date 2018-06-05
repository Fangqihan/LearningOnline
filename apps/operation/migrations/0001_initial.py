# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-11 15:44
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CourseComments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=150, verbose_name='课程评论')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
            options={
                'verbose_name_plural': '用户课程评论',
                'verbose_name': '用户课程评论',
            },
        ),
        migrations.CreateModel(
            name='UserAsk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('mobile', models.CharField(max_length=10, verbose_name='联系电话')),
                ('course', models.CharField(max_length=20, verbose_name='咨询课程')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
            options={
                'verbose_name_plural': '用户咨询',
                'verbose_name': '用户咨询',
            },
        ),
        migrations.CreateModel(
            name='UserCourses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
            options={
                'verbose_name_plural': '用户学习课程',
                'verbose_name': '用户学习课程',
            },
        ),
        migrations.CreateModel(
            name='UserFavorite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('favor_type', models.IntegerField(choices=[(3, '课程机构'), (2, '机构教师'), (1, '公开课程')], verbose_name='用户收藏类型')),
                ('favor_id', models.IntegerField(default=0, verbose_name='收藏id')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
            options={
                'verbose_name_plural': '用户收藏',
                'verbose_name': '用户收藏',
            },
        ),
        migrations.CreateModel(
            name='UserMessages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('has_read', models.BooleanField(default=False, verbose_name='是否已读')),
                ('message', models.CharField(max_length=50, verbose_name='用户消息')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
            options={
                'verbose_name_plural': '用户消息',
                'verbose_name': '用户消息',
            },
        ),
    ]