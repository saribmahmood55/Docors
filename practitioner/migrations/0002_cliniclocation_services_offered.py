# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('practitioner', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliniclocation',
            name='services_offered',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
