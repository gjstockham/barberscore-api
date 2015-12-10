# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import phonenumber_field.modelfields
import model_utils.fields
import apps.api.validators
import autoslug.fields
import mptt.fields
import django.core.validators
import django.utils.timezone
import apps.api.models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0019_auto_20151206_2352'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('id', models.UUIDField(default=uuid.uuid4, serialize=False, editable=False, primary_key=True)),
                ('name', models.CharField(help_text=b'\n            The name of the resource.', max_length=200, unique=True, error_messages={b'unique': b'The name must be unique.  Add middle initials, suffixes, years, or other identifiers to make the name unique.'}, validators=[apps.api.validators.validate_trimmed])),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from=b'name', max_length=255, always_update=True, unique=True)),
                ('start_date', models.DateField(help_text=b'\n            The founding/birth date of the resource.', null=True, blank=True)),
                ('end_date', models.DateField(help_text=b'\n            The retirement/deceased date of the resource.', null=True, blank=True)),
                ('location', models.CharField(help_text=b'\n            The geographical location of the resource.', max_length=200, blank=True)),
                ('website', models.URLField(help_text=b'\n            The website URL of the resource.', blank=True)),
                ('facebook', models.URLField(help_text=b'\n            The facebook URL of the resource.', blank=True)),
                ('twitter', models.CharField(blank=True, help_text=b'\n            The twitter handle (in form @twitter_handle) of the resource.', max_length=16, validators=[django.core.validators.RegexValidator(regex=b'@([A-Za-z0-9_]+)', message=b'\n                    Must be a single Twitter handle\n                    in the form `@twitter_handle`.\n                ')])),
                ('email', models.EmailField(help_text=b'\n            The contact email of the resource.', max_length=254, blank=True)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(help_text=b'\n            The phone number of the resource.  Include country code.', max_length=128, null=True, blank=True)),
                ('picture', models.ImageField(help_text=b'\n            The picture/logo of the resource.', null=True, upload_to=apps.api.models.generate_image_filename, blank=True)),
                ('description', models.TextField(help_text=b'\n            A description/bio of the resource.  Max 1000 characters.', max_length=1000, blank=True)),
                ('notes', models.TextField(help_text=b'\n            Notes (for internal use only).', blank=True)),
                ('is_active', models.BooleanField(default=True, help_text=b'\n            A boolean for active/living resources.')),
                ('status', models.IntegerField(default=0, choices=[(0, b'New'), (10, b'Active'), (20, b'Inactive')])),
                ('status_monitor', model_utils.fields.MonitorField(default=django.utils.timezone.now, help_text=b'Status last updated', monitor=b'status')),
                ('code', models.CharField(help_text=b'\n            The chapter code (only for choruses).', max_length=200, blank=True)),
                ('organization', mptt.fields.TreeForeignKey(related_name='chapters', blank=True, to='api.Organization', null=True)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.AddField(
            model_name='group',
            name='chapter',
            field=models.ForeignKey(related_name='groups', blank=True, to='api.Chapter', null=True),
        ),
    ]