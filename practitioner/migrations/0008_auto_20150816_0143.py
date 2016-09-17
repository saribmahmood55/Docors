# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('practitioner', '0007_auto_20150719_1324'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='practitioner',
            options={'ordering': ('-modified',), 'verbose_name_plural': 'Practitioners'},
        ),
    ]
