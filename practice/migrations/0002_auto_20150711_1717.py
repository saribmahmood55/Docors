# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('practice', '0001_initial'),
        ('practitioner', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recentsearch',
            name='specialty',
            field=models.ForeignKey(to='practitioner.Specialization'),
        ),
        migrations.AddField(
            model_name='practicetiming',
            name='practice',
            field=models.ForeignKey(to='practice.Practice'),
        ),
        migrations.AddField(
            model_name='practicelocation',
            name='area',
            field=models.ForeignKey(to='practice.Area'),
        ),
        migrations.AddField(
            model_name='practice',
            name='fee',
            field=models.ForeignKey(blank=True, to='practice.CheckupFee', null=True),
        ),
        migrations.AddField(
            model_name='practice',
            name='practice_location',
            field=models.ForeignKey(to='practice.PracticeLocation'),
        ),
        migrations.AddField(
            model_name='practice',
            name='practitioner',
            field=models.ForeignKey(to='practitioner.Practitioner'),
        ),
        migrations.AddField(
            model_name='area',
            name='city',
            field=models.ForeignKey(to='practice.City'),
        ),
    ]
