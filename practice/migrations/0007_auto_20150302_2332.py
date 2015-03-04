# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('practice', '0006_auto_20150127_1309'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='practice',
            name='practice_photo',
        ),
        migrations.AddField(
            model_name='practicelocation',
            name='photo',
            field=sorl.thumbnail.fields.ImageField(null=True, upload_to=b'practice/', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='practice',
            name='practice_type',
            field=models.CharField(help_text=b'Practice Type', max_length=1, choices=[(b'P', b'Private Clinic/Residence'), (b'H', b'Hospital'), (b'M', b'Medical Complex')]),
        ),
    ]
