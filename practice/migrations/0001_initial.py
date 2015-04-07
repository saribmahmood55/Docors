# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import autoslug.fields
import sorl.thumbnail.fields
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('practitioner', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CheckupFee',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('amount', models.PositiveSmallIntegerField()),
            ],
            options={
                'verbose_name_plural': 'CheckupFee',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('slug', autoslug.fields.AutoSlugField(unique=True, editable=False)),
            ],
            options={
                'verbose_name_plural': 'Cities',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Practice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('practice_type', models.CharField(help_text=b'Practice Type', max_length=1, choices=[(b'P', b'Private Clinic/Residence'), (b'H', b'Hospital'), (b'M', b'Medical Complex')])),
                ('services', models.TextField(null=True, blank=True)),
                ('appointments_only', models.BooleanField(default=True)),
                ('location', django.contrib.gis.db.models.fields.PointField(srid=4326, null=True, geography=True, blank=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('fee', models.ForeignKey(blank=True, to='practice.CheckupFee', null=True)),
            ],
            options={
                'verbose_name_plural': 'Practice',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PracticeLocation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('slug', autoslug.fields.AutoSlugField(unique=True, editable=False)),
                ('contact_number', models.CharField(max_length=150, null=True, blank=True)),
                ('photo', sorl.thumbnail.fields.ImageField(null=True, upload_to=b'practice/', blank=True)),
                ('clinic_address', models.TextField()),
                ('lon', models.FloatField(null=True, blank=True)),
                ('lat', models.FloatField(null=True, blank=True)),
                ('city', models.ForeignKey(to='practice.City')),
            ],
            options={
                'verbose_name_plural': 'Practice Locations',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PracticeTiming',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('day', models.CharField(help_text=b'Select Day.', max_length=1, choices=[(b'1', b'Mon'), (b'2', b'Tue'), (b'3', b'Wed'), (b'4', b'Thu'), (b'5', b'Fri'), (b'6', b'Sat'), (b'7', b'Sun')])),
                ('start_time', models.TimeField(help_text=b'Select starting Time for Clininc.', null=True, blank=True)),
                ('end_time', models.TimeField(help_text=b'Select ending Time for Clininc.', null=True, blank=True)),
                ('practice', models.ForeignKey(to='practice.Practice')),
                ('practitioner', models.ForeignKey(to='practitioner.Practitioner')),
            ],
            options={
                'verbose_name_plural': 'Practice Timings',
            },
            bases=(models.Model,),
        ),
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
        migrations.AddField(
            model_name='practice',
            name='practice_location',
            field=models.ForeignKey(to='practice.PracticeLocation'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='practice',
            name='practitioner',
            field=models.ForeignKey(to='practitioner.Practitioner'),
            preserve_default=True,
        ),
    ]
