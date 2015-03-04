# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('practitioner', '0009_auto_20150302_2332'),
    ]

    operations = [
        migrations.CreateModel(
            name='Degree',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=25)),
                ('points', models.PositiveSmallIntegerField(default=0)),
            ],
            options={
                'verbose_name_plural': 'Degrees',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='practitioner',
            name='degrees',
            field=models.ManyToManyField(to='practitioner.Degree'),
            preserve_default=True,
        ),
    ]
