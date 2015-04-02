# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('practice', '0008_auto_20150321_1325'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='practicetiming',
            name='end_time',
        ),
        migrations.RemoveField(
            model_name='practicetiming',
            name='start_time',
        ),
    ]
