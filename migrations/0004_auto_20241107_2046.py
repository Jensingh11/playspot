# Generated by Django 3.2.7 on 2024-11-07 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20241107_2029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='turf',
            name='timing_end',
            field=models.TimeField(default='22:00:00'),
        ),
        migrations.AlterField(
            model_name='turf',
            name='timing_start',
            field=models.TimeField(default='06:00:00'),
        ),
    ]
