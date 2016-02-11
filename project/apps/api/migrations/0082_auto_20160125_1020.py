# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-25 18:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0081_auto_20160124_2142'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='bhs_contact',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='group',
            name='bhs_district',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='group',
            name='bhs_expiration',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='group',
            name='bhs_location',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='group',
            name='bhs_name',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='group',
            name='group_id',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]