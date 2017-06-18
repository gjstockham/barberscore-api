# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-12 05:30
from __future__ import unicode_literals

from django.db import migrations
import django_fsm


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0022_auto_20170611_2224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='repertory',
            name='status',
            field=django_fsm.FSMIntegerField(choices=[(0, 'New')], default=0),
        ),
    ]