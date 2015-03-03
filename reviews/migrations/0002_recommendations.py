# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '__first__'),
        ('practitioner', '0009_auto_20150302_2332'),
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recommendations',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', models.BooleanField(default=False)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('patient', models.ForeignKey(to='patients.Patient')),
                ('practitioner', models.ForeignKey(to='practitioner.Practitioner')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
