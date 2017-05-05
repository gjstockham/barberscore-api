# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-08 18:57
from __future__ import unicode_literals

from django.db import migrations


def forwards(apps, schema_editor):
    Repertory = apps.get_model("app", "Repertory")
    reps = Repertory.objects.all()
    reps.delete()

    Chart = apps.get_model("app", "Chart")
    cs = Chart.objects.all()
    cs.delete()


def backwards(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20170428_1312'),
    ]

    operations = [
        migrations.RunPython(forwards, backwards),
    ]