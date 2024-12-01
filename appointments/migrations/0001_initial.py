# Generated by Django 4.2.16 on 2024-12-01 17:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Timetable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day_of_visit', models.PositiveSmallIntegerField(choices=[(0, 'Monday'), (1, 'Tuesday'), (2, 'Wednesday'), (3, 'Thursday'), (4, 'Friday'), (5, 'Saturday'), (6, 'Sunday')], unique=True, verbose_name='День приема')),
                ('doctor', models.ManyToManyField(to=settings.AUTH_USER_MODEL, verbose_name='Врач')),
            ],
            options={
                'verbose_name': 'Расписание',
                'verbose_name_plural': 'Расписания',
            },
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Дата')),
                ('time', models.TimeField(verbose_name='Время')),
                ('status_of_appointment', models.CharField(choices=[('WAITING', 'ожидание приема'), ('COMPLETED', 'прием оказан'), ('CANCELLED', 'прием отменен')], default='WAITING', max_length=20)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('price', models.FloatField(verbose_name='Цена')),
                ('doctor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='appointments_as_doctor', to=settings.AUTH_USER_MODEL, verbose_name='врач')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='appointments_as_user', to=settings.AUTH_USER_MODEL, verbose_name='пациент')),
            ],
            options={
                'verbose_name': 'Запись',
                'verbose_name_plural': 'Записи',
            },
        ),
    ]
