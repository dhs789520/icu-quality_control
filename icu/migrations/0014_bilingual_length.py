# Generated by Django 2.0.5 on 2019-03-12 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('icu', '0013_bilingual'),
    ]

    operations = [
        migrations.AddField(
            model_name='bilingual',
            name='length',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
