# Generated by Django 4.2.16 on 2024-12-16 19:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('appointments', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DoctorWorkingTime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.CharField(max_length=5, unique=True, verbose_name='Время')),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Доктор')),
            ],
            options={
                'verbose_name': 'Часы работы доктора',
                'verbose_name_plural': 'Часы работы доктора',
            },
        ),
        migrations.AddField(
            model_name='timetable',
            name='doctor_work_time',
            field=models.ManyToManyField(to='appointments.doctorworkingtime', verbose_name='Часы работы врача'),
        ),
    ]
