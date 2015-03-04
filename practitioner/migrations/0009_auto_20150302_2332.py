# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('practitioner', '0008_practitioner_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='practitioner',
            name='physician_type',
            field=models.PositiveSmallIntegerField(blank=True, help_text=b'Physician type', null=True, choices=[(1, b'Trainee'), (2, b'Specialist')]),
        ),
        migrations.AlterField(
            model_name='practitioner',
            name='title',
            field=models.PositiveSmallIntegerField(blank=True, null=True, choices=[(1, b'Dr. '), (2, b'Prof. '), (3, b'Prof. Dr. ')]),
        ),
    ]
