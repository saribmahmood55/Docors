# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import autoslug.fields


class Migration(migrations.Migration):

    dependencies = [
        ('practitioner', '0002_cliniclocation_services_offered'),
    ]

    operations = [
        migrations.AddField(
            model_name='practitioner',
            name='slug',
            field=autoslug.fields.AutoSlugField(default=b'', editable=False),
            preserve_default=True,
        ),
    ]
