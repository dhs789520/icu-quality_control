# Generated by Django 2.0.5 on 2019-02-21 11:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('notebook', '0015_user_company'),
        ('icu', '0006_auto_20190220_1911'),
    ]

    operations = [
        migrations.CreateModel(
            name='QualityControl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.IntegerField()),
                ('entry', models.IntegerField()),
                ('outpatient', models.IntegerField()),
                ('shiftIn', models.IntegerField()),
                ('unplannedShift', models.IntegerField()),
                ('revert', models.IntegerField()),
                ('out', models.IntegerField()),
                ('transfer', models.IntegerField()),
                ('improve', models.IntegerField()),
                ('cure', models.IntegerField()),
                ('automaticDischarge', models.IntegerField()),
                ('death', models.IntegerField()),
                ('septicShock', models.IntegerField()),
                ('bundle3', models.IntegerField()),
                ('bundle6', models.IntegerField()),
                ('tracheaCannula', models.IntegerField()),
                ('newTracheaCannula', models.IntegerField()),
                ('unplannedExtubation', models.IntegerField()),
                ('reintubation', models.IntegerField()),
                ('ventilation', models.IntegerField()),
                ('newVAP', models.IntegerField()),
                ('AVCatheter', models.IntegerField()),
                ('newAVCatheter', models.IntegerField()),
                ('CRBSI', models.IntegerField()),
                ('urethralCatheter', models.IntegerField()),
                ('newUrethralCatheter', models.IntegerField()),
                ('CAUTI', models.IntegerField()),
                ('antibiotic', models.IntegerField()),
                ('sample', models.IntegerField()),
                ('preventDVT', models.IntegerField()),
                ('newDVT', models.IntegerField()),
                ('comments', models.CharField(max_length=400)),
                ('doctor', models.CharField(max_length=40)),
                ('ip', models.CharField(max_length=40)),
                ('scoreDate', models.DateField(verbose_name='质控日期')),
                ('createTime', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updateTime', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notebook.User')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]
