# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('practice', '0004_auto_20141107_1433'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='practice',
            name='checkup_on_waiting',
        ),
    ]
