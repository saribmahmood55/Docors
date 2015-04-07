# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('practitioner', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cell_number', models.CharField(help_text=b'Please use the following format: 03215555555', max_length=20, null=True, blank=True)),
                ('gender', models.CharField(blank=True, max_length=1, null=True, help_text=b'Please select gender.', choices=[(b'M', b'Male'), (b'F', b'Female')])),
                ('age_group', models.CharField(blank=True, max_length=2, null=True, help_text=b'Please select appropriate age group.', choices=[(b'10', b'10-14'), (b'15', b'15-19'), (b'20', b'20-24'), (b'25', b'25-29'), (b'30', b'30-34'), (b'35', b'35-39'), (b'40', b'40-44'), (b'45', b'45-49'), (b'50', b'50-54'), (b'55', b'55-59'), (b'60', b'60-64'), (b'65', b'65-69'), (b'70', b'70-74'), (b'75', b'75-79'), (b'80', b'80-84'), (b'85', b'85+')])),
                ('favt_practitioner', models.ManyToManyField(to='practitioner.Practitioner')),
                ('interested_specialities', models.ManyToManyField(to='practitioner.Specialization')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Patients',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cell_number', models.CharField(max_length=20, null=True, blank=True)),
                ('email', models.EmailField(max_length=35, null=True, blank=True)),
                ('practitioner', models.ForeignKey(to='practitioner.Practitioner')),
            ],
            options={
                'verbose_name_plural': 'Subscriptions',
            },
            bases=(models.Model,),
        ),
    ]
