# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('practitioner', '0013_auto_20150902_1151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='practitioner',
            name='review_rating',
            field=models.DecimalField(default=0.0, max_digits=4, decimal_places=2),
        ),
    ]
