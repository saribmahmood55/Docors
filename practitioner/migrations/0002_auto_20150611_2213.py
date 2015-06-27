# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('practitioner', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('condition', models.CharField(max_length=150)),
                ('procedure', models.CharField(max_length=150)),
                ('speciality', models.ForeignKey(to='practitioner.Specialization')),
            ],
            options={
                'verbose_name_plural': 'Services',
            },
        ),
        migrations.AddField(
            model_name='practitioner',
            name='services',
            field=models.ManyToManyField(to='practitioner.Service'),
        ),
    ]
