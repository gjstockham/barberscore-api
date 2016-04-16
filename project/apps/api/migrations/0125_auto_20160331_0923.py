# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-31 16:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0124_auto_20160329_1223'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='award',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='certification',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='chapter',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='contest',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='contestant',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='convention',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='group',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='judge',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='member',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='organization',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='performance',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='performer',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='person',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='role',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='round',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='score',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='session',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='song',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='submission',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='venue',
            name='slug',
        ),
        migrations.AlterField(
            model_name='contest',
            name='champion',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='contests', to='api.Contestant'),
        ),
    ]