# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('practitioner', '0004_condition_procedure'),
    ]

    operations = [
        migrations.AddField(
            model_name='practitioner',
            name='conditions',
            field=models.ManyToManyField(to='practitioner.Condition'),
        ),
        migrations.AddField(
            model_name='practitioner',
            name='procedures',
            field=models.ManyToManyField(to='practitioner.Procedure'),
        ),
    ]
