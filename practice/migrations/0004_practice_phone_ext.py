# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('practice', '0003_auto_20150715_1652'),
    ]

    operations = [
        migrations.AddField(
            model_name='practice',
            name='phone_ext',
            field=models.CharField(max_length=150, null=True, verbose_name=b'Extension no.', blank=True),
        ),
    ]
