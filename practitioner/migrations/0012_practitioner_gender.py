# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('practitioner', '0011_auto_20150305_2241'),
    ]

    operations = [
        migrations.AddField(
            model_name='practitioner',
            name='gender',
            field=models.CharField(default=b'M', max_length=1, choices=[(b'M', b'Male'), (b'F', b'Female')]),
            preserve_default=True,
        ),
    ]
