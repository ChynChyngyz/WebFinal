# Generated by Django 5.1.3 on 2024-11-16 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Speciality',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('speciality_name', models.CharField(max_length=30, unique=True)),
                ('description', models.TextField(blank=True, max_length=30)),
                ('image', models.ImageField(blank=True, null=True, upload_to='image_speciality/', verbose_name='Изображение')),
            ],
            options={
                'verbose_name': 'Специализация',
                'verbose_name_plural': 'Специализации',
            },
        ),
    ]
