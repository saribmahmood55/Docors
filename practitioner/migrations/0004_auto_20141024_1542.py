# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import autoslug.fields


class Migration(migrations.Migration):

    dependencies = [
        ('practitioner', '0003_auto_20141023_1720'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='practise',
            options={'verbose_name_plural': 'Practise'},
        ),
        migrations.AddField(
            model_name='practiselocation',
            name='slug',
            field=autoslug.fields.AutoSlugField(unique=True, null=True, editable=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='city',
            name='slug',
            field=autoslug.fields.AutoSlugField(unique=True, editable=False),
        ),
        migrations.AlterField(
            model_name='specialization',
            name='slug',
            field=autoslug.fields.AutoSlugField(unique=True, editable=False),
        ),
    ]
