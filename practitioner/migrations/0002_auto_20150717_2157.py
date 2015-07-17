# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('practitioner', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='practitioner',
            name='completion_year',
            field=models.PositiveIntegerField(default=0, verbose_name=b'Fellowship expected in year.'),
        ),
        migrations.AlterField(
            model_name='practitioner',
            name='experience',
            field=models.PositiveIntegerField(default=0, help_text=b'Number of years'),
        ),
    ]
