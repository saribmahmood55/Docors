# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('practice', '0004_practice_phone_ext'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='checkupfee',
            options={'ordering': ('amount',), 'verbose_name_plural': 'Checkup Fee'},
        ),
        migrations.AlterField(
            model_name='practice',
            name='phone_ext',
            field=models.CharField(default=None, max_length=150, null=True, verbose_name=b'Extension no.', blank=True),
        ),
    ]
