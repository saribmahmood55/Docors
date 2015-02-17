# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('practitioner', '0006_practitioner_physician_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='practitioner',
            name='not_recommended',
            field=models.PositiveIntegerField(default=0),
            preserve_default=True,
        ),
    ]
