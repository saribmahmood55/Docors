# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('practitioner', '0005_auto_20150719_1243'),
    ]

    operations = [
        migrations.AddField(
            model_name='updateinfo',
            name='approved',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='updateinfo',
            name='ip',
            field=models.CharField(max_length=255, verbose_name=b'IP address or Email'),
        ),
    ]
