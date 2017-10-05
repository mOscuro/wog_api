# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-10-05 13:50
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('wog_round', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Progression',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sessions', to=settings.AUTH_USER_MODEL)),
                ('users', models.ManyToManyField(related_name='athletes', to=settings.AUTH_USER_MODEL)),
            ],
        ),
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
        migrations.AddField(
            model_name='session',
            name='workout',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wog_workout.Workout'),
        ),
        migrations.AddField(
            model_name='progression',
            name='session',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wog_workout.Session'),
        ),
        migrations.AddField(
            model_name='progression',
            name='step',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wog_round.Step'),
        ),
        migrations.AddField(
            model_name='progression',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='workout',
            unique_together=set([('creator', 'name')]),
        ),
    ]