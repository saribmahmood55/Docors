# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='reviewstats',
            options={'verbose_name_plural': 'Reviews Status'},
        ),
        migrations.AlterField(
            model_name='reviewstats',
            name='status',
            field=models.IntegerField(default=0),
        ),
    ]
