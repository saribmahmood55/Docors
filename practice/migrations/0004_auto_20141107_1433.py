# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('practice', '0003_practice_next_available_appointment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='practice',
            name='next_available_appointment',
            field=models.DateField(null=True, blank=True),
        ),
    ]
