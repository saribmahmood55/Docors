# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0001_initial'),
        ('practice', '0001_initial'),
        ('practitioner', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscription',
            name='practitioner',
            field=models.ForeignKey(to='practitioner.Practitioner'),
        ),
        migrations.AddField(
            model_name='patient',
            name='city',
            field=models.ForeignKey(default=1, to='practice.City'),
        ),
        migrations.AddField(
            model_name='patient',
            name='favt_practitioner',
            field=models.ManyToManyField(to='practitioner.Practitioner', blank=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='interested_specialities',
            field=models.ManyToManyField(to='practitioner.Specialization', blank=True),
        ),
    ]
