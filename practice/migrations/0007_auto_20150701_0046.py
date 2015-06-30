# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('practice', '0006_auto_20150630_1150'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='area',
            options={'ordering': ('name',), 'verbose_name_plural': 'Areas'},
        ),
        migrations.AlterModelOptions(
            name='city',
            options={'ordering': ('name',), 'verbose_name_plural': 'Cities'},
        ),
    ]
