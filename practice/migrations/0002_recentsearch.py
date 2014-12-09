# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('practitioner', '0003_practitioner_recommendation'),
        ('practice', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RecentSearch',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hit_count', models.PositiveIntegerField(default=0)),
                ('city', models.ForeignKey(to='practice.City')),
                ('speciality', models.ForeignKey(to='practitioner.Specialization')),
            ],
            options={
                'verbose_name_plural': 'Recent Searches',
            },
            bases=(models.Model,),
        ),
    ]
