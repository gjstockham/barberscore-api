# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-29 05:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0089_auto_20160128_0957'),
    ]

    operations = [
        migrations.AddField(
            model_name='score',
            name='is_flagged',
            field=models.NullBooleanField(),
        ),
    ]
