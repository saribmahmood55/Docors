# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0003_auto_20141025_0120'),
        ('practitioner', '0004_auto_20141024_1542'),
    ]

    operations = [
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
                ('practise', models.ForeignKey(to='practitioner.Practise', null=True)),
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
