# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-11 04:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0021_auto_20170410_2128'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appearance',
            old_name='total_points',
            new_name='tot_points',
        ),
        migrations.RenameField(
            model_name='appearance',
            old_name='total_score',
            new_name='tot_score',
        ),
        migrations.RenameField(
            model_name='appearanceprivate',
            old_name='total_points',
            new_name='tot_points',
        ),
        migrations.RenameField(
            model_name='appearanceprivate',
            old_name='total_score',
            new_name='tot_score',
        ),
        migrations.RenameField(
            model_name='contestant',
            old_name='total_points',
            new_name='tot_points',
        ),
        migrations.RenameField(
            model_name='contestant',
            old_name='total_score',
            new_name='tot_score',
        ),
        migrations.RenameField(
            model_name='contestantprivate',
            old_name='total_points',
            new_name='tot_points',
        ),
        migrations.RenameField(
            model_name='contestantprivate',
            old_name='total_score',
            new_name='tot_score',
        ),
        migrations.RenameField(
            model_name='entry',
            old_name='total_points',
            new_name='tot_points',
        ),
        migrations.RenameField(
            model_name='entry',
            old_name='total_score',
            new_name='tot_score',
        ),
        migrations.RenameField(
            model_name='entryprivate',
            old_name='total_points',
            new_name='tot_points',
        ),
        migrations.RenameField(
            model_name='entryprivate',
            old_name='total_score',
            new_name='tot_score',
        ),
        migrations.RenameField(
            model_name='song',
            old_name='total_points',
            new_name='tot_points',
        ),
        migrations.RenameField(
            model_name='song',
            old_name='total_score',
            new_name='tot_score',
        ),
        migrations.RenameField(
            model_name='songprivate',
            old_name='total_points',
            new_name='tot_points',
        ),
        migrations.RenameField(
            model_name='songprivate',
            old_name='total_score',
            new_name='tot_score',
        ),
    ]