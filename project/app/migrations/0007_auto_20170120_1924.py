# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-21 03:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20170120_1921'),
    ]

    operations = [
        migrations.RenameField('Performer', 'tenor_new', 'tenor'),
        migrations.RenameField('Performer', 'lead_new', 'lead'),
        migrations.RenameField('Performer', 'baritone_new', 'baritone'),
        migrations.RenameField('Performer', 'bass_new', 'bass'),
        migrations.RenameField('Performer', 'director_new', 'director'),
        migrations.RenameField('Performer', 'codirector_new', 'codirector'),
    ]
