# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-02 20:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0058_auto_20160302_1210'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='award',
            options={'ordering': ('level', 'is_primary', 'kind', 'size')},
        ),
        migrations.RemoveField(
            model_name='group',
            name='is_chorus',
        ),
        migrations.RemoveField(
            model_name='group',
            name='is_collegiate',
        ),
        migrations.RemoveField(
            model_name='group',
            name='is_quartet',
        ),
        migrations.RemoveField(
            model_name='group',
            name='is_senior',
        ),
        migrations.RemoveField(
            model_name='group',
            name='is_youth',
        ),
        migrations.AlterUniqueTogether(
            name='award',
            unique_together=set([('organization', 'is_improved', 'size', 'idiom', 'kind')]),
        ),
        migrations.AlterUniqueTogether(
            name='session',
            unique_together=set([('convention', 'kind')]),
        ),
    ]
