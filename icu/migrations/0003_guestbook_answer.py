# Generated by Django 2.0.5 on 2018-10-28 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('icu', '0002_auto_20181028_1126'),
    ]

    operations = [
        migrations.AddField(
            model_name='guestbook',
            name='answer',
            field=models.TextField(null=True),
        ),
    ]
