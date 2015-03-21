# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('practice', '0007_auto_20150302_2332'),
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
        migrations.RemoveField(
            model_name='practice',
            name='checkup_fee',
        ),
        migrations.RemoveField(
            model_name='practice',
            name='contact_number',
        ),
        migrations.AddField(
            model_name='practice',
            name='fee',
            field=models.ForeignKey(blank=True, to='practice.CheckupFee', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='practicelocation',
            name='contact_number',
            field=models.CharField(max_length=150, null=True, blank=True),
            preserve_default=True,
        ),
    ]
