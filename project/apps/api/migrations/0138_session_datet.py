# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-08 16:49
from __future__ import unicode_literals

import django.contrib.postgres.fields.ranges
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0137_auto_20160408_0946'),
    ]

    operations = [
        migrations.AddField(
            model_name='session',
            name='datet',
            field=django.contrib.postgres.fields.ranges.DateTimeRangeField(blank=True, help_text=b'\n            The active dates of the session.', null=True),
        ),
    ]
