# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-21 05:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20160220_2030'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='bhs_address',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='organization',
            name='bhs_chapter_code',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='organization',
            name='bhs_chapter_name',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='organization',
            name='bhs_city',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='organization',
            name='bhs_contact',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='organization',
            name='bhs_district',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='organization',
            name='bhs_group_id',
            field=models.IntegerField(blank=True, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='organization',
            name='bhs_group_name',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='organization',
            name='bhs_name',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='organization',
            name='bhs_phone',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='organization',
            name='bhs_state',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='organization',
            name='bhs_venue',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='organization',
            name='bhs_website',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='organization',
            name='bhs_zip',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='organization',
            name='code',
            field=models.CharField(blank=True, help_text=b'\n            The chapter code.', max_length=200, null=True),
        ),
    ]