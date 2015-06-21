# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('practitioner', '0005_auto_20150618_0152'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='practitioner',
            name='title',
        ),
    ]
