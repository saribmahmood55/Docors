# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('practitioner', '0006_remove_practitioner_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='practitioner',
            name='conditions',
            field=models.ManyToManyField(to='practitioner.Condition', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='practitioner',
            name='procedures',
            field=models.ManyToManyField(to='practitioner.Procedure', null=True, blank=True),
        ),
    ]
