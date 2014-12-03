# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import autoslug.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Practitioner',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('slug', autoslug.fields.AutoSlugField(unique=True, editable=False)),
                ('credentials', models.TextField()),
                ('achievements', models.TextField(null=True, blank=True)),
                ('experience', models.PositiveIntegerField(help_text=b'Number of years')),
                ('message', models.TextField(max_length=140, null=True, blank=True)),
                ('status', models.BooleanField(default=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Specialization',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('human_name', models.CharField(max_length=100, null=True)),
                ('slug', autoslug.fields.AutoSlugField(unique=True, editable=False)),
            ],
            options={
                'verbose_name_plural': 'Specialities',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='practitioner',
            name='specialities',
            field=models.ManyToManyField(to='practitioner.Specialization'),
            preserve_default=True,
        ),
    ]
