# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-30 20:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_auto_20170530_0911'),
    ]

    operations = [
        migrations.AddField(
            model_name='office',
            name='is_drcj',
            field=models.BooleanField(default=False),
        ),
    ]