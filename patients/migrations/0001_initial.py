# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('docorsauth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('docorsuser_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('cell_number', models.BigIntegerField(help_text=b'Mobile phone number e.g. 03001234567', unique=True, blank=True, validators=[django.core.validators.MaxValueValidator(3500000000, message=b'Please enter a valid mobile phone number e.g. 03001234567'), django.core.validators.MinValueValidator(3000000000, message=b'Please enter a valid mobile phone number e.g. 03001234567')])),
            ],
            options={
                'verbose_name_plural': 'Patients',
            },
            bases=('docorsauth.docorsuser',),
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cell_number', models.CharField(max_length=20, null=True, blank=True)),
                ('email', models.EmailField(max_length=35, null=True, blank=True)),
            ],
            options={
                'verbose_name_plural': 'Subscriptions',
            },
        ),
    ]
