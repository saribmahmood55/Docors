# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('practitioner', '0003_practitioner_recommendation'),
    ]

    operations = [
        migrations.AddField(
            model_name='specialization',
            name='SEO_name',
            field=models.CharField(max_length=100, null=True),
            preserve_default=True,
        ),
    ]
