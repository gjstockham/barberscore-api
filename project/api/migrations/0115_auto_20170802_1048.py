# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-02 17:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0114_auto_20170802_1010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(editable=False, max_length=254, unique=True),
        ),
    ]
