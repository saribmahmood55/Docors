# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('practice', '0005_auto_20150719_1243'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='practicetiming',
            name='day',
        ),
        migrations.AlterField(
            model_name='practicetiming',
            name='end_time',
            field=models.TimeField(help_text=b'Select ending Time for Clinic.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='practicetiming',
            name='start_time',
            field=models.TimeField(help_text=b'Select starting Time for Clinic.', null=True, blank=True),
        ),
    ]
