# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-20 19:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0030_auto_20160520_1052'),
    ]

    operations = [
        migrations.AddField(
            model_name='performer',
            name='is_private',
            field=models.BooleanField(default=False, help_text=b'\n            Keep scores private.'),
        ),
    ]