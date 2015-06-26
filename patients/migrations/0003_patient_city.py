# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('practice', '0005_auto_20150618_0344'),
        ('patients', '0002_auto_20150611_2211'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='city',
            field=models.ForeignKey(default=1, to='practice.City'),
        ),
    ]
