# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('practitioner', '0007_auto_20150628_1618'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='condition',
            options={'ordering': ('name',), 'verbose_name_plural': 'Conditions'},
        ),
        migrations.AlterModelOptions(
            name='degree',
            options={'ordering': ('name',), 'verbose_name_plural': 'Degrees'},
        ),
        migrations.AlterModelOptions(
            name='fellowship',
            options={'ordering': ('name',), 'verbose_name_plural': 'Fellowships'},
        ),
        migrations.AlterModelOptions(
            name='practitioner',
            options={'ordering': ('name',), 'verbose_name_plural': 'Practitioner'},
        ),
        migrations.AlterModelOptions(
            name='procedure',
            options={'ordering': ('name',), 'verbose_name_plural': 'Procedures'},
        ),
        migrations.AlterModelOptions(
            name='specialization',
            options={'ordering': ('name',), 'verbose_name_plural': 'Specialities'},
        ),
        migrations.AlterField(
            model_name='practitioner',
            name='physician_type',
            field=models.CharField(max_length=1, null=True, choices=[(b'0', b'General Physician'), (b'1', b'Trainee'), (b'2', b'Specialist')]),
        ),
        migrations.AlterField(
            model_name='practitioner',
            name='review_rating',
            field=models.DecimalField(default=0.0, max_digits=2, decimal_places=2),
        ),
    ]
