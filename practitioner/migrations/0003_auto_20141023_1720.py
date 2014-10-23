# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import autoslug.fields


class Migration(migrations.Migration):

    dependencies = [
        ('practitioner', '0002_auto_20141023_1716'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='practiselocation',
            name='slug',
        ),
        migrations.AddField(
            model_name='city',
            name='slug',
            field=autoslug.fields.AutoSlugField(unique=True, null=True, editable=False),
            preserve_default=True,
        ),
    ]
