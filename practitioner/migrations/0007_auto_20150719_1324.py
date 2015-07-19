# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('practitioner', '0006_auto_20150719_1302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='updateinfo',
            name='ip',
            field=models.CharField(max_length=255, null=True, verbose_name=b'IP address or Email', blank=True),
        ),
    ]
