# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('practitioner', '0002_practitioner_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='practitioner',
            name='recommendation',
            field=models.PositiveIntegerField(default=0),
            preserve_default=True,
        ),
    ]
