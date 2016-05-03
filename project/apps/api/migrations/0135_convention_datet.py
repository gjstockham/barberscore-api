# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-08 15:52
from __future__ import unicode_literals

import django.contrib.postgres.fields.ranges
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0134_auto_20160406_0837'),
    ]

    operations = [
        migrations.AddField(
            model_name='convention',
            name='datet',
            field=django.contrib.postgres.fields.ranges.DateTimeRangeField(blank=True, help_text=b'\n            The scheduled time frame for the convention.', null=True),
        ),
    ]
