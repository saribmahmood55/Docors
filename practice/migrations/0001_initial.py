# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import autoslug.fields
import sorl.thumbnail.fields
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('slug', autoslug.fields.AutoSlugField(unique=True, editable=False)),
            ],
            options={
                'ordering': ('name',),
                'verbose_name_plural': 'Areas',
            },
        ),
        migrations.CreateModel(
            name='CheckupFee',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('amount', models.PositiveSmallIntegerField()),
            ],
            options={
                'verbose_name_plural': 'CheckupFee',
            },
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('slug', autoslug.fields.AutoSlugField(unique=True, editable=False)),
            ],
            options={
                'ordering': ('name',),
                'verbose_name_plural': 'Cities',
            },
        ),
        migrations.CreateModel(
            name='Practice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('practice_type', models.CharField(help_text=b'Practice Type', max_length=1, choices=[(b'P', b'Private Clinic/Residence'), (b'H', b'Hospital'), (b'M', b'Medical Complex')])),
                ('appointments_only', models.BooleanField(default=True)),
                ('location', django.contrib.gis.db.models.fields.PointField(srid=4326, null=True, geography=True, blank=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Practice',
            },
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
            ],
            options={
                'verbose_name_plural': 'Practice Locations',
            },
        ),
        migrations.CreateModel(
            name='PracticeTiming',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('day', models.CharField(help_text=b'Select Day.', max_length=1, choices=[(b'1', b'Mon'), (b'2', b'Tue'), (b'3', b'Wed'), (b'4', b'Thu'), (b'5', b'Fri'), (b'6', b'Sat'), (b'7', b'Sun')])),
                ('start_time', models.TimeField(help_text=b'Select starting Time for Clininc.', null=True, blank=True)),
                ('end_time', models.TimeField(help_text=b'Select ending Time for Clininc.', null=True, blank=True)),
            ],
            options={
                'verbose_name_plural': 'Practice Timings',
            },
        ),
        migrations.CreateModel(
            name='RecentSearch',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hit_count', models.PositiveIntegerField(default=0)),
                ('city', models.ForeignKey(to='practice.City')),
            ],
            options={
                'verbose_name_plural': 'Recent Searches',
            },
        ),
    ]
