# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-22 02:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0137_auto_20160721_1933'),
    ]

    operations = [
        migrations.RenameField(
            model_name='performer',
            old_name='district',
            new_name='representing',
        ),
    ]