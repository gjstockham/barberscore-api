# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-07 20:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20170407_1303'),
    ]

    operations = [
        migrations.RenameField(
            model_name='repertory',
            old_name='catalog',
            new_name='chart',
        ),
        migrations.RenameField(
            model_name='song',
            old_name='catalog',
            new_name='chart',
        ),
        migrations.AlterField(
            model_name='submission',
            name='bhs_id',
            field=models.IntegerField(blank=True, help_text='\n            The BHS Chart Number.\n        ', null=True),
        ),
        migrations.AlterUniqueTogether(
            name='repertory',
            unique_together=set([('entity', 'chart')]),
        ),
    ]