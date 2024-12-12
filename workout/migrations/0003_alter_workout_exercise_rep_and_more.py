# Generated by Django 4.2.16 on 2024-12-08 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workout', '0002_workout_workout_exercise'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workout_exercise',
            name='rep',
            field=models.PositiveSmallIntegerField(default=10),
        ),
        migrations.AlterField(
            model_name='workout_exercise',
            name='sets',
            field=models.PositiveSmallIntegerField(default=3),
        ),
    ]