# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('practice', '0009_auto_20150403_0103'),
    ]

    operations = [
        migrations.AddField(
            model_name='practicetiming',
            name='end_time',
            field=models.TimeField(help_text=b'Select ending Time for Clininc.', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='practicetiming',
            name='start_time',
            field=models.TimeField(help_text=b'Select starting Time for Clininc.', null=True, blank=True),
            preserve_default=True,
        ),
    ]
