# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('practitioner', '0004_specialization_seo_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='practitioner',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
