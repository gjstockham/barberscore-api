# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-03 20:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0083_auto_20160303_1244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='award',
            name='scope',
            field=models.IntegerField(blank=True, choices=[(100, b'Plateau 1'), (110, b'Plateau 2'), (120, b'Plateau 3'), (130, b'Plateau 4'), (140, b'Plateau A'), (150, b'Plateau AA'), (160, b'Plateau AAA'), (170, b'Plateau AAAA'), (175, b'Plateau AAAAA')], null=True),
        ),
    ]