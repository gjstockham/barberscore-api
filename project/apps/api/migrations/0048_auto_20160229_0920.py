# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-29 17:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0047_auto_20160229_0826'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='convention',
            unique_together=set([('organization', 'season', 'year', 'division')]),
        ),
    ]