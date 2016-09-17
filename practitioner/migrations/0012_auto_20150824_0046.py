# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('practitioner', '0011_auto_20150821_0035'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='specialization',
            options={'ordering': ('name',), 'verbose_name_plural': 'Specialties'},
        ),
        migrations.AddField(
            model_name='fellowship',
            name='human_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='specialization',
            name='training_region',
            field=models.CharField(max_length=3, null=True, choices=[(b'All', b'All'), (b'Pak', b'Pakistan'), (b'Eur', b'Europe/UK'), (b'USA', b'United States')]),
        ),
    ]
