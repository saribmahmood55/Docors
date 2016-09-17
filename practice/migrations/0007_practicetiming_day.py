# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('practice', '0006_auto_20150823_0025'),
    ]

    operations = [
        migrations.AddField(
            model_name='practicetiming',
            name='day',
            field=models.PositiveSmallIntegerField(default=0, help_text=b'Select Day.', choices=[(0, 'Monday'), (1, 'Tuesday'), (2, 'Wednesday'), (3, 'Thursday'), (4, 'Friday'), (5, 'Saturday'), (6, 'Sunday')]),
        ),
    ]
