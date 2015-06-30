# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('practice', '0005_auto_20150618_0344'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recentsearch',
            old_name='speciality',
            new_name='specialty',
        ),
    ]
