# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-21 21:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_contest_parent'),
    ]

    operations = [
        migrations.AddField(
            model_name='award',
            name='season',
            field=models.IntegerField(blank=True, choices=[(1, b'Fall'), (2, b'Spring')], null=True),
        ),
    ]