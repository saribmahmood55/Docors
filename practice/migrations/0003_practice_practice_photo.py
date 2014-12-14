# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('practice', '0002_recentsearch'),
    ]

    operations = [
        migrations.AddField(
            model_name='practice',
            name='practice_photo',
            field=models.ImageField(null=True, upload_to=b'practice/photo/', blank=True),
            preserve_default=True,
        ),
    ]
