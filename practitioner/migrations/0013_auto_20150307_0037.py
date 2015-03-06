# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('practitioner', '0012_practitioner_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='practitioner',
            name='education_marks',
            field=models.PositiveIntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='practitioner',
            name='photo',
            field=sorl.thumbnail.fields.ImageField(null=True, upload_to=b'practitioner/', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='practitioner',
            name='year_of_birth',
            field=models.PositiveIntegerField(default=0),
            preserve_default=True,
        ),
    ]
