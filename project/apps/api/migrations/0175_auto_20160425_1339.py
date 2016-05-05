# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-25 20:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0174_auto_20160425_0905'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='id_name',
            field=models.CharField(blank=True, editable=False, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='judge',
            name='certification',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='judges', to='api.Certification'),
        ),
    ]
