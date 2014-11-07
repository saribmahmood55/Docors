# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('practice', '0002_practice_checkup_on_waiting'),
    ]

    operations = [
        migrations.AddField(
            model_name='practice',
            name='next_available_appointment',
            field=models.DateTimeField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
