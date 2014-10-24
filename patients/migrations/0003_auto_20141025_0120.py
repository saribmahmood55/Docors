# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0002_auto_20141023_1716'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='practitionerreview',
            name='patient',
        ),
        migrations.RemoveField(
            model_name='practitionerreview',
            name='practitioner',
        ),
        migrations.RemoveField(
            model_name='reviewstats',
            name='patient',
        ),
        migrations.RemoveField(
            model_name='reviewstats',
            name='review',
        ),
        migrations.DeleteModel(
            name='PractitionerReview',
        ),
        migrations.DeleteModel(
            name='ReviewStats',
        ),
    ]
