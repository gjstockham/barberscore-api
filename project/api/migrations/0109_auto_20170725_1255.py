# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-25 19:55
from __future__ import unicode_literals

from django.db import migrations
import django_fsm


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0108_auto_20170724_1443'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session',
            name='status',
            field=django_fsm.FSMIntegerField(choices=[(0, 'New'), (2, 'Published'), (4, 'Opened'), (8, 'Closed'), (10, 'Verified'), (20, 'Started'), (30, 'Finished'), (45, 'Announced'), (95, 'Archived')], default=0),
        ),
    ]
