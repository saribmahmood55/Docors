# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('practitioner', '0003_remove_practitioner_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Claim',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.EmailField(help_text='Verification email will be sent at this address. So please ensure you enter correct email', max_length=255, verbose_name=b'email address')),
                ('pmdc_no', models.CharField(max_length=b'20')),
                ('photo', sorl.thumbnail.fields.ImageField(help_text='Please provide a passport size photograph of yours to help in the verification process.', null=True, upload_to=b'practitioner/', blank=True)),
                ('current_status', models.BooleanField(default=False)),
                ('practitioner', models.ForeignKey(to='practitioner.Practitioner')),
            ],
            options={
                'ordering': ('email',),
                'verbose_name_plural': 'Practitioner Claims',
            },
        ),
    ]
