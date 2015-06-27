# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('practice', '0004_remove_practice_services'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='practicelocation',
            name='city',
        ),
        migrations.AddField(
            model_name='practicelocation',
            name='area',
            field=models.ForeignKey(default=4, to='practice.Area'),
            preserve_default=False,
        ),
    ]
