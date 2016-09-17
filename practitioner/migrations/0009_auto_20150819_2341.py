# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('practitioner', '0008_auto_20150816_0143'),
    ]

    operations = [
        migrations.AddField(
            model_name='fellowship',
            name='description',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='specialization',
            name='description',
            field=models.TextField(null=True, blank=True),
        ),
    ]
