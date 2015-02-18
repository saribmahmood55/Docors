# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('practitioner', '0007_practitioner_not_recommended'),
    ]

    operations = [
        migrations.AddField(
            model_name='practitioner',
            name='title',
            field=models.PositiveSmallIntegerField(blank=True, null=True, choices=[(b'1', b'Dr. '), (b'2', b'Prof. '), (b'3', b'Prof. Dr. ')]),
            preserve_default=True,
        ),
    ]
