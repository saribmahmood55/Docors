# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import autoslug.fields


class Migration(migrations.Migration):

    dependencies = [
        ('practitioner', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='practiselocation',
            name='slug',
            field=autoslug.fields.AutoSlugField(unique=True, null=True, editable=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='specialization',
            name='slug',
            field=autoslug.fields.AutoSlugField(unique=True, null=True, editable=False),
            preserve_default=True,
        ),
    ]
