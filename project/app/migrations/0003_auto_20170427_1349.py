# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-27 20:49
from __future__ import unicode_literals

import app.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20170427_1339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entity',
            name='image',
            field=app.fields.CloudinaryRenameField(blank=True, max_length=255, null=True, verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='entry',
            name='image',
            field=app.fields.CloudinaryRenameField(blank=True, max_length=255, null=True, verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='person',
            name='image',
            field=app.fields.CloudinaryRenameField(blank=True, max_length=255, null=True, verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='session',
            name='scoresheet',
            field=app.fields.CloudinaryRenameField(blank=True, max_length=255, null=True, verbose_name='raw'),
        ),
    ]
