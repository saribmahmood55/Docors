# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('practice', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='practice',
            name='checkup_on_waiting',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
    ]
