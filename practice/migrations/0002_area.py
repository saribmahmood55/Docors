# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import autoslug.fields


class Migration(migrations.Migration):

    dependencies = [
        ('practice', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('slug', autoslug.fields.AutoSlugField(unique=True, editable=False)),
                ('city', models.ForeignKey(to='practice.City')),
            ],
            options={
                'verbose_name_plural': 'Areas',
            },
        ),
    ]
