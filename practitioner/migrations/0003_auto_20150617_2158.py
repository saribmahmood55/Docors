# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('practitioner', '0002_auto_20150611_2213'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='speciality',
        ),
        migrations.RemoveField(
            model_name='practitioner',
            name='services',
        ),
        migrations.DeleteModel(
            name='Service',
        ),
    ]
