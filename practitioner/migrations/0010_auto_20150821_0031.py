# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('practitioner', '0009_auto_20150819_2341'),
    ]

    operations = [
        migrations.AddField(
            model_name='condition',
            name='Fellowship',
            field=models.ForeignKey(blank=True, to='practitioner.Fellowship', null=True),
        ),
        migrations.AddField(
            model_name='procedure',
            name='Fellowship',
            field=models.ForeignKey(blank=True, to='practitioner.Fellowship', null=True),
        ),
    ]
