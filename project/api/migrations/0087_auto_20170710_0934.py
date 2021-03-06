# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-10 16:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0086_auto_20170710_0931'),
    ]

    operations = [
        migrations.AddField(
            model_name='office',
            name='is_award_manager',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='office',
            name='is_organization_manager',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='office',
            name='is_person_manager',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='office',
            name='is_session_manager',
            field=models.BooleanField(default=False),
        ),
    ]
