# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('practice', '0002_auto_20150711_1717'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='practice',
            name='location',
        ),
        migrations.AddField(
            model_name='practicelocation',
            name='location',
            field=django.contrib.gis.db.models.fields.PointField(srid=4326, null=True, geography=True, blank=True),
        ),
    ]
