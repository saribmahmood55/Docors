# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import autoslug.fields
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('practitioner', '__first__'),
    ]

    operations = [
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
                ('practice_type', models.CharField(help_text=b'Practice Type', max_length=1, choices=[(b'P', b'Private Clininc'), (b'H', b'Hospital')])),
                ('contact_number', models.CharField(max_length=100)),
                ('checkup_fee', models.PositiveIntegerField()),
                ('services', models.TextField(null=True, blank=True)),
                ('appointments_only', models.BooleanField(default=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('location', django.contrib.gis.db.models.fields.PointField(srid=4326, null=True, geography=True, blank=True)),
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
                ('day', models.CharField(help_text=b'Select Day.', max_length=3, choices=[(b'Mon', b'Monday'), (b'Tue', b'Tuesday'), (b'Wed', b'Wednesday'), (b'Thu', b'Thursday'), (b'Fri', b'Friday'), (b'Sat', b'Saturday'), (b'Sun', b'Sunday')])),
                ('start_time', models.CharField(help_text=b'Select starting Time for Clininc.', max_length=5, choices=[(b'7', b'07:00am'), (b'7.5', b'07:30am'), (b'8', b'08:00am'), (b'8.5', b'08:30am'), (b'9', b'09:00am'), (b'9.5', b'09:30am'), (b'10', b'10:00am'), (b'10.5', b'10:30am'), (b'11', b'11:00am'), (b'11.5', b'11:30am'), (b'12', b'12:00pm'), (b'12.5', b'12:30pm'), (b'13', b'01:00pm'), (b'13.5', b'01:30pm'), (b'14', b'02:00pm'), (b'14.5', b'02:30am'), (b'15', b'03:00pm'), (b'15.5', b'03:30pm'), (b'16', b'04:00pm'), (b'16.5', b'04:30pm'), (b'17', b'05:00pm'), (b'17.5', b'05:30pm'), (b'18', b'06:00pm'), (b'18.5', b'06:30pm'), (b'19', b'07:00pm'), (b'19.5', b'07:30pm'), (b'20', b'08:00pm'), (b'20.5', b'08:30pm'), (b'21', b'09:00pm'), (b'21.5', b'09:30pm'), (b'22', b'10:00pm'), (b'22.5', b'10:30pm'), (b'23', b'11:00pm'), (b'23.5', b'11:30pm'), (b'0', b'12:00am'), (b'0.5', b'12:30am'), (b'1', b'01:00am'), (b'2', b'02:00am'), (b'2.5', b'02:30am')])),
                ('end_time', models.CharField(help_text=b'Select ending Time for Clininc.', max_length=5, choices=[(b'7', b'07:00am'), (b'7.5', b'07:30am'), (b'8', b'08:00am'), (b'8.5', b'08:30am'), (b'9', b'09:00am'), (b'9.5', b'09:30am'), (b'10', b'10:00am'), (b'10.5', b'10:30am'), (b'11', b'11:00am'), (b'11.5', b'11:30am'), (b'12', b'12:00pm'), (b'12.5', b'12:30pm'), (b'13', b'01:00pm'), (b'13.5', b'01:30pm'), (b'14', b'02:00pm'), (b'14.5', b'02:30am'), (b'15', b'03:00pm'), (b'15.5', b'03:30pm'), (b'16', b'04:00pm'), (b'16.5', b'04:30pm'), (b'17', b'05:00pm'), (b'17.5', b'05:30pm'), (b'18', b'06:00pm'), (b'18.5', b'06:30pm'), (b'19', b'07:00pm'), (b'19.5', b'07:30pm'), (b'20', b'08:00pm'), (b'20.5', b'08:30pm'), (b'21', b'09:00pm'), (b'21.5', b'09:30pm'), (b'22', b'10:00pm'), (b'22.5', b'10:30pm'), (b'23', b'11:00pm'), (b'23.5', b'11:30pm'), (b'0', b'12:00am'), (b'0.5', b'12:30am'), (b'1', b'01:00am'), (b'2', b'02:00am'), (b'2.5', b'02:30am')])),
                ('practice', models.ForeignKey(to='practice.Practice')),
                ('practitioner', models.ForeignKey(to='practitioner.Practitioner')),
            ],
            options={
                'verbose_name_plural': 'Practice Timings',
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
