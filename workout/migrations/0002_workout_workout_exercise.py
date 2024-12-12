# Generated by Django 4.2.16 on 2024-12-08 17:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('workout', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkOut',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('is_private', models.BooleanField(default=True)),
                ('is_active', models.BooleanField(default=True)),
                ('planed', models.DateTimeField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('C', 'Created'), ('P', 'planned'), ('D', 'Done'), ('I', 'In Progress')], default='C', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='WorkOut_Exercise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rep', models.PositiveSmallIntegerField()),
                ('sets', models.PositiveSmallIntegerField()),
                ('Exercise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workout.exercise')),
                ('WorkOut', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workout.workout')),
            ],
        ),
    ]