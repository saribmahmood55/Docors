# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('practitioner', '0004_claim'),
    ]

    operations = [
        migrations.CreateModel(
            name='UpdateInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ip', models.CharField(max_length=12, verbose_name=b'IP address')),
                ('incorrect_info', models.CharField(max_length=1, null=True, choices=[(b'1', b'Physican Type'), (b'2', b'Experience'), (b'3', b'Achievements'), (b'4', b'Degree'), (b'5', b'Speciality'), (b'6', b'Fellowship'), (b'7', b'Completion Year'), (b'8', b'Conditions'), (b'9', b'Procedures')])),
                ('correct_info', models.CharField(max_length=150)),
                ('comments', models.CharField(max_length=150, null=True, blank=True)),
                ('practitioner', models.ForeignKey(to='practitioner.Practitioner')),
            ],
            options={
                'ordering': ('practitioner',),
                'verbose_name': 'Update Info',
            },
        ),
        migrations.AlterField(
            model_name='claim',
            name='pmdc_no',
            field=models.CharField(max_length=20),
        ),
    ]
