# Generated by Django 2.0.5 on 2018-10-28 03:15

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='guestbook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact', models.CharField(max_length=500, null=True)),
                ('content', models.TextField()),
                ('public', models.BooleanField(default=False)),
                ('createTime', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
