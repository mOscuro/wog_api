# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-04-03 14:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('workout', '0001_initial'),
        ('exercise', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Round',
            fields=[
                ('workouttree_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='workout.WorkoutTree')),
                ('nb_repeat', models.IntegerField(default=1)),
                ('_workout', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rounds', to='workout.Workout')),
            ],
            options={
                'abstract': False,
            },
            bases=('workout.workouttree',),
        ),
        migrations.CreateModel(
            name='Step',
            fields=[
                ('workouttree_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='workout.WorkoutTree')),
                ('nb_rep', models.IntegerField(default=1)),
                ('distance', models.IntegerField(default=0)),
                ('weight', models.FloatField(default=0)),
                ('rest_time', models.IntegerField(default=0)),
                ('_round', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='round_steps', to='round.Round')),
                ('_workout', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wod_step', to='workout.Workout')),
                ('exercise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exercise.Exercise')),
            ],
            options={
                'abstract': False,
            },
            bases=('workout.workouttree',),
        ),
    ]
