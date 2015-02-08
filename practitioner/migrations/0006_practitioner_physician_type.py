# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('practitioner', '0005_auto_20150127_1309'),
    ]

    operations = [
        migrations.AddField(
            model_name='practitioner',
            name='physician_type',
            field=models.PositiveSmallIntegerField(blank=True, help_text=b'Physician type', null=True, choices=[(b'1', b'Trainee'), (b'2', b'Specialist')]),
            preserve_default=True,
        ),
    ]
