# Generated by Django 4.2.16 on 2024-12-07 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authUser', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='phone',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='Телефон'),
        ),
    ]
