# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-21 06:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20160220_2250'),
    ]

    operations = [
        migrations.AddField(
            model_name='contestant',
            name='contest',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='contestants', to='api.Contest'),
        ),
    ]