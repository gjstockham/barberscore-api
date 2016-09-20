# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-18 19:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0122_auto_20160718_1129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='convention',
            name='drcj',
            field=models.ForeignKey(blank=True, help_text=b'\n            The person managing the convention.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='conventions', to='api.Person'),
        ),
        migrations.AlterField(
            model_name='convention',
            name='kind',
            field=models.IntegerField(blank=True, choices=[(10, b'International'), (20, b'District'), (30, b'Division'), (40, b'District and Division'), (200, b'EVG Division I'), (210, b'EVG Division II'), (220, b'EVG Division III'), (230, b'EVG Division IV'), (240, b'EVG Division V'), (250, b'FWD Arizona Division'), (260, b'FWD NE/NW Divisions'), (270, b'FWD SE/SW Divisions'), (280, b'LOL Division One/Packerland Divisions'), (290, b'LOL Northern Plains Division'), (300, b'LOL 10,000 Lakes and Southwest Divisions'), (322, b'MAD Northern Division'), (324, b'MAD Central Division'), (330, b'MAD Southern Division'), (340, b'NED Sunrise Division'), (342, b'NED Western Regional'), (344, b'NED Eastern Regional'), (350, b'SWD NE/NW/SE/SW Divisions')], null=True),
        ),
        migrations.AlterField(
            model_name='convention',
            name='organization',
            field=mptt.fields.TreeForeignKey(blank=True, help_text=b'\n            The organization hosting the convention.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='conventions', to='api.Organization'),
        ),
    ]