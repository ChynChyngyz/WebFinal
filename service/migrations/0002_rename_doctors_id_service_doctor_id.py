# Generated by Django 4.2.16 on 2024-12-01 17:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='service',
            old_name='doctors_id',
            new_name='doctor_id',
        ),
    ]
