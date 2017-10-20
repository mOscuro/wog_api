# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-20 21:45
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Workout',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('time_cap', models.IntegerField(default=0)),
                ('amrap', models.IntegerField(default=0)),
                ('emom', models.IntegerField(default=0)),
                ('description', models.TextField(blank=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_public', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='workouts', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'permissions': (('view_workout', 'Can view the workout and its content'),),
            },
        ),
        migrations.CreateModel(
            name='WorkoutProgression',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('step', models.IntegerField()),
                ('time', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='WorkoutSession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('start', models.DateTimeField()),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sessions', to=settings.AUTH_USER_MODEL)),
                ('workout', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='session_groups', to='wog_workout.Workout')),
            ],
            options={
                'permissions': (('session_view', 'Can view session but not interact with progression'), ('session_watch', 'Can only read progression for the session'), ('session_perform', 'Can read, create or delete progression')),
            },
        ),
        migrations.AddField(
            model_name='workoutprogression',
            name='session',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wog_workout.WorkoutSession'),
        ),
        migrations.AddField(
            model_name='workoutprogression',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='workoutprogression',
            unique_together=set([('user', 'session', 'step')]),
        ),
        migrations.AlterUniqueTogether(
            name='workout',
            unique_together=set([('creator', 'name')]),
        ),
    ]
