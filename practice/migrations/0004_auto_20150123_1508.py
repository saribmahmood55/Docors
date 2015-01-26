# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('practice', '0003_practice_practice_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='practice',
            name='practice_photo',
            field=sorl.thumbnail.fields.ImageField(null=True, upload_to=b'practice/', blank=True),
        ),
    ]
