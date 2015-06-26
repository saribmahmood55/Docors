# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('practice', '0003_remove_practicetiming_practitioner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='practice',
            name='services',
        ),
    ]
