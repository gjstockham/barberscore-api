# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-28 19:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0181_auto_20160427_1850'),
    ]

    operations = [
        migrations.AlterField(
            model_name='judge',
            name='category',
            field=models.IntegerField(choices=[(0, b'Admin'), (1, b'Music'), (2, b'Presentation'), (3, b'Singing')]),
        ),
        migrations.AlterField(
            model_name='judge',
            name='kind',
            field=models.IntegerField(choices=[(10, b'Official'), (12, b'CA'), (14, b'ACA'), (20, b'Practice'), (30, b'Composite')]),
        ),
    ]