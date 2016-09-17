# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('practitioner', '0014_auto_20150905_1336'),
    ]

    operations = [
        migrations.AddField(
            model_name='claim',
            name='prescription_photo',
            field=sorl.thumbnail.fields.ImageField(help_text='Please provide a passport size photograph of yours to help             in the verification process.', null=True, upload_to=b'practitioner/claim/prescription_photo/', blank=True),
        ),
        migrations.AlterField(
            model_name='claim',
            name='email',
            field=models.EmailField(help_text='Verification email will be sent at this address. So please             ensure you enter correct email', max_length=255, verbose_name=b'email address'),
        ),
        migrations.AlterField(
            model_name='claim',
            name='photo',
            field=sorl.thumbnail.fields.ImageField(help_text='Please provide a passport size photograph of yours to help             in the verification process.', null=True, upload_to=b'practitioner/claim/photo/', blank=True),
        ),
        migrations.AlterField(
            model_name='specialization',
            name='training_region',
            field=models.CharField(max_length=10, null=True, choices=[(b'all', b'All'), (b'pak', b'Asia'), (b'eur', b'Europe/UK'), (b'usa', b'United States'), (b'pak_eur', b'Pakistan/Europe'), (b'pak_usa', b'Pakistan/USA'), (b'eur_usa', b'Europe/USA')]),
        ),
    ]
