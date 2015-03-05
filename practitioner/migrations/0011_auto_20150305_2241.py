# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('practitioner', '0010_auto_20150305_0156'),
    ]

    operations = [
        migrations.AddField(
            model_name='degree',
            name='color_code',
            field=models.CharField(max_length=10, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='degree',
            name='description',
            field=models.CharField(max_length=250, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='degree',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
