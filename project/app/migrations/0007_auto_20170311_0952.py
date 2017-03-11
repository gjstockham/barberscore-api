# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-11 17:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20170311_0949'),
    ]

    operations = [
        migrations.AlterField(
            model_name='convention',
            name='entity',
            field=models.ForeignKey(help_text='\n            The owning entity for the convention.', on_delete=django.db.models.deletion.CASCADE, related_name='conventions', to='app.Entity'),
        ),
    ]
