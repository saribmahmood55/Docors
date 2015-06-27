# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('practice', '0002_area'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='practicetiming',
            name='practitioner',
        ),
    ]
