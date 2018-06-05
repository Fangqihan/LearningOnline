# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-11 15:44
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('organization', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='chapter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='章节名')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='课程添加时间')),
            ],
            options={
                'verbose_name_plural': '章节',
                'verbose_name': '章节',
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='课程名')),
                ('description', models.CharField(max_length=100, verbose_name='课程描述')),
                ('detail', models.TextField(verbose_name='课程详情')),
                ('degree', models.CharField(choices=[('CJ', '初级'), ('ZJ', '中级'), ('GJ', '高级')], max_length=10)),
                ('learn_times', models.IntegerField(default=0, verbose_name='学习时长')),
                ('students_num', models.IntegerField(default=0, verbose_name='学习人数')),
                ('category', models.CharField(max_length=20, verbose_name='课程类别')),
                ('favor_num', models.IntegerField(default=0, verbose_name='收藏数')),
                ('image', models.ImageField(upload_to='course/%Y/%m', verbose_name='课程图片')),
                ('click_num', models.IntegerField(default=0, verbose_name='点击数')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='课程添加时间')),
                ('org', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organization.CourseOrg', verbose_name='所属课程机构')),
            ],
            options={
                'verbose_name_plural': '课程',
                'verbose_name': '课程',
            },
        ),
        migrations.CreateModel(
            name='CourseResource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='资料名称')),
                ('download', models.FileField(upload_to='course/download/%Y/%m', verbose_name='资源文件')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.Course')),
            ],
            options={
                'verbose_name_plural': '课程资源下载',
                'verbose_name': '课程资源下载',
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='视频名')),
                ('url', models.URLField(verbose_name='视频链接')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='课程添加时间')),
                ('chapter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.Course', verbose_name='所属章节')),
            ],
            options={
                'verbose_name_plural': '视频',
                'verbose_name': '视频',
            },
        ),
        migrations.AddField(
            model_name='chapter',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.Course', verbose_name='所属课程'),
        ),
    ]
