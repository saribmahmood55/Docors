# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('practice', '0005_auto_20150126_1405'),
    ]

    operations = [
        migrations.AlterField(
            model_name='practicetiming',
            name='day',
            field=models.CharField(help_text=b'Select Day.', max_length=1, choices=[(b'1', b'Mon'), (b'2', b'Tue'), (b'3', b'Wed'), (b'4', b'Thu'), (b'5', b'Fri'), (b'6', b'Sat'), (b'7', b'Sun')]),
        ),
    ]
