# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='favt_practitioner',
            field=models.ManyToManyField(to='practitioner.Practitioner', blank=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='gender',
            field=models.CharField(blank=True, max_length=1, null=True, help_text=b'Please select gender.', choices=[(b'M', b'Male'), (b'F', b'Female'), (b'N', b'Prefer not to disclose')]),
        ),
        migrations.AlterField(
            model_name='patient',
            name='interested_specialities',
            field=models.ManyToManyField(to='practitioner.Specialization', blank=True),
        ),
    ]
