# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-21 21:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0039_auto_20170621_0710'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='convention',
            name='kind',
        ),
        migrations.RemoveField(
            model_name='convention',
            name='level',
        ),
    ]
