# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import autoslug.fields


class Migration(migrations.Migration):

    dependencies = [
        ('practitioner', '0003_auto_20150617_2158'),
    ]

    operations = [
        migrations.CreateModel(
            name='Condition',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('slug', autoslug.fields.AutoSlugField(unique=True, editable=False)),
                ('specialization', models.ForeignKey(to='practitioner.Specialization')),
            ],
            options={
                'verbose_name_plural': 'Conditions',
            },
        ),
        migrations.CreateModel(
            name='Procedure',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('slug', autoslug.fields.AutoSlugField(unique=True, editable=False)),
                ('specialization', models.ForeignKey(to='practitioner.Specialization')),
            ],
            options={
                'verbose_name_plural': 'Procedures',
            },
        ),
    ]
