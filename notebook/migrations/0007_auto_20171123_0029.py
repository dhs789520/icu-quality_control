# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-23 00:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notebook', '0006_auto_20171024_0817'),
    ]

    operations = [
        migrations.RenameField(
            model_name='note',
            old_name='base_document',
            new_name='base_dir',
        ),
    ]