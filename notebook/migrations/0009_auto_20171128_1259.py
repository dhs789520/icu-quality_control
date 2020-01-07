# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-11-28 04:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('notebook', '0008_auto_20171123_0054'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='note',
            name='click_time',
        ),
        migrations.AddField(
            model_name='note',
            name='click_times',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='note',
            name='create_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='note',
            name='delete_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='note',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='note',
            name='retrieve_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='note',
            name='share',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='note',
            name='share_passwd',
            field=models.CharField(max_length=25, null=True),
        ),
        migrations.AddField(
            model_name='note',
            name='update_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='user',
            name='create_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='user',
            name='real_name',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='sort_rank',
            field=models.IntegerField(default=0),
        ),
    ]
