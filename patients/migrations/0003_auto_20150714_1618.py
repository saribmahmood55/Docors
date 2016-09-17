# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0002_auto_20150711_1717'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='cell_number',
            field=models.BigIntegerField(blank=True, help_text=b'Mobile phone number e.g. 03001234567', unique=True, null=True, validators=[django.core.validators.MaxValueValidator(3500000000, message=b'Please enter a valid mobile phone number e.g. 03001234567'), django.core.validators.MinValueValidator(3000000000, message=b'Please enter a valid mobile phone number e.g. 03001234567')]),
        ),
    ]
