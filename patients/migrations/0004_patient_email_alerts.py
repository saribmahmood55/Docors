# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0003_auto_20150714_1618'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='email_alerts',
            field=models.BooleanField(default=True),
        ),
    ]
