# Generated by Django 4.2.10 on 2024-02-23 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('managements', '0005_choices_alter_bus_arrival_city_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='bus',
            name='depart_time',
            field=models.TimeField(null=True),
        ),
    ]
