# Generated by Django 5.1.3 on 2024-11-20 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('speciality', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('slug', models.SlugField(blank=True, max_length=255, unique=True)),
            ],
        ),
    ]