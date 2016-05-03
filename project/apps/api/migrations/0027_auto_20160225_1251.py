# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-25 20:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0026_contest_is_qualifier'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contest',
            options={'ordering': ('-session__convention__year', 'award', 'session')},
        ),
        migrations.RemoveField(
            model_name='contestant',
            name='award',
        ),
        migrations.RemoveField(
            model_name='performer',
            name='is_chorus',
        ),
        migrations.RemoveField(
            model_name='performer',
            name='is_collegiate',
        ),
        migrations.RemoveField(
            model_name='performer',
            name='is_novice',
        ),
        migrations.RemoveField(
            model_name='performer',
            name='is_quartet',
        ),
        migrations.RemoveField(
            model_name='performer',
            name='is_senior',
        ),
        migrations.RemoveField(
            model_name='performer',
            name='is_youth',
        ),
        migrations.RemoveField(
            model_name='session',
            name='is_chorus',
        ),
        migrations.RemoveField(
            model_name='session',
            name='is_collegiate',
        ),
        migrations.RemoveField(
            model_name='session',
            name='is_novice',
        ),
        migrations.RemoveField(
            model_name='session',
            name='is_quartet',
        ),
        migrations.RemoveField(
            model_name='session',
            name='is_senior',
        ),
        migrations.RemoveField(
            model_name='session',
            name='is_youth',
        ),
    ]
