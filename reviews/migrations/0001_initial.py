# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('practitioner', '0001_initial'),
        ('patients', '0001_initial'),
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
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('post_as_anonymous', models.BooleanField(default=False)),
                ('review_text', models.TextField()),
                ('review_date', models.DateTimeField(auto_now_add=True)),
                ('up_votes', models.PositiveIntegerField(default=0)),
                ('down_votes', models.PositiveIntegerField(default=0)),
                ('patient', models.ForeignKey(to='patients.Patient')),
                ('practitioner', models.ForeignKey(to='practitioner.Practitioner')),
            ],
            options={
                'verbose_name_plural': 'Reviews',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ReviewStats',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.IntegerField(default=0)),
                ('patient', models.ForeignKey(to='patients.Patient')),
                ('review', models.ForeignKey(to='reviews.Review')),
            ],
            options={
                'verbose_name_plural': 'Reviews Status',
            },
            bases=(models.Model,),
        ),
    ]
