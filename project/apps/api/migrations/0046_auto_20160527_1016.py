# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-27 17:16
from __future__ import unicode_literals

from django.db import migrations
import django_fsm


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0045_auto_20160527_1012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contestant',
            name='status',
            field=django_fsm.FSMIntegerField(choices=[(0, b'New'), (10, b'Eligible'), (20, b'Ineligible'), (40, b'District Representative'), (50, b'Qualified'), (55, b'Validated'), (60, b'Finished'), (70, b'Scratched'), (80, b'Disqualified')], default=0),
        ),
    ]