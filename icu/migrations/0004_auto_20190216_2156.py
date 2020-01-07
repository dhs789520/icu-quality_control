# Generated by Django 2.0.5 on 2019-02-16 13:56

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('notebook', '0015_user_company'),
        ('icu', '0003_guestbook_answer'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApacheII',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('age', models.IntegerField()),
                ('bedNumber', models.CharField(max_length=20)),
                ('inNumber', models.IntegerField()),
                ('temperature', models.FloatField()),
                ('SBP', models.IntegerField()),
                ('DBP', models.IntegerField()),
                ('MAP', models.FloatField()),
                ('HR', models.IntegerField()),
                ('R', models.IntegerField()),
                ('WBC', models.FloatField()),
                ('HCT', models.FloatField()),
                ('pH', models.FloatField()),
                ('FiO2', models.FloatField()),
                ('PaO2', models.FloatField()),
                ('PaCO2', models.FloatField()),
                ('AaDO2', models.FloatField()),
                ('Na', models.FloatField()),
                ('K', models.FloatField()),
                ('Cr', models.FloatField()),
                ('AKI', models.CharField(max_length=4)),
                ('health', models.CharField(max_length=40)),
                ('E', models.IntegerField()),
                ('V', models.IntegerField()),
                ('M', models.IntegerField()),
                ('noSurgery', models.CharField(max_length=40)),
                ('surgery', models.CharField(max_length=40)),
                ('afterSurgery', models.CharField(max_length=20)),
                ('score', models.FloatField()),
                ('deathRate', models.FloatField()),
                ('doctor', models.CharField(max_length=40)),
                ('ip', models.CharField(max_length=40)),
                ('scoreTime', models.CharField(max_length=40)),
                ('createTime', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notebook.User')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.RenameField(
            model_name='guestbook',
            old_name='createTime',
            new_name='create_time',
        ),
    ]
