# Generated by Django 5.0.7 on 2025-04-14 11:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0002_alter_weather_options_alter_weather_city_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='weather',
            name='weather_description',
        ),
    ]
