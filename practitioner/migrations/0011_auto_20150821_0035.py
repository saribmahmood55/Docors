# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('practitioner', '0010_auto_20150821_0031'),
    ]

    operations = [
        migrations.RenameField(
            model_name='condition',
            old_name='Fellowship',
            new_name='fellowship',
        ),
        migrations.RenameField(
            model_name='procedure',
            old_name='Fellowship',
            new_name='fellowship',
        ),
    ]
