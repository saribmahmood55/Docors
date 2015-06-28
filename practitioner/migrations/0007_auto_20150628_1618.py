# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import autoslug.fields


class Migration(migrations.Migration):

    dependencies = [
        ('practitioner', '0006_remove_practitioner_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fellowship',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('slug', autoslug.fields.AutoSlugField(unique=True, editable=False)),
                ('specialization', models.ForeignKey(to='practitioner.Specialization')),
            ],
            options={
                'verbose_name_plural': 'Fellowships',
            },
        ),
        migrations.RemoveField(
            model_name='practitioner',
            name='specialities',
        ),
        migrations.AddField(
            model_name='practitioner',
            name='review_rating',
            field=models.DecimalField(null=True, max_digits=2, decimal_places=2),
        ),
        migrations.AddField(
            model_name='practitioner',
            name='specialty',
            field=models.ForeignKey(blank=True, to='practitioner.Specialization', null=True),
        ),
        migrations.AlterField(
            model_name='practitioner',
            name='conditions',
            field=models.ManyToManyField(to='practitioner.Condition', blank=True),
        ),
        migrations.AlterField(
            model_name='practitioner',
            name='message',
            field=models.CharField(max_length=140, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='practitioner',
            name='physician_type',
            field=models.CharField(max_length=1, null=True, choices=[(0, b'General Physician'), (1, b'Trainee'), (2, b'Specialist')]),
        ),
        migrations.AlterField(
            model_name='practitioner',
            name='procedures',
            field=models.ManyToManyField(to='practitioner.Procedure', blank=True),
        ),
        migrations.AddField(
            model_name='practitioner',
            name='fellowship',
            field=models.ManyToManyField(to='practitioner.Fellowship', blank=True),
        ),
    ]
