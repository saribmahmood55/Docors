# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import autoslug.fields
import sorl.thumbnail.fields
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('docorsauth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Condition',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('slug', autoslug.fields.AutoSlugField(unique=True, editable=False)),
            ],
            options={
                'ordering': ('name',),
                'verbose_name_plural': 'Conditions',
            },
        ),
        migrations.CreateModel(
            name='Degree',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('points', models.PositiveSmallIntegerField(default=0)),
                ('color_code', models.CharField(max_length=10, null=True, blank=True)),
                ('description', models.CharField(max_length=250, null=True, blank=True)),
            ],
            options={
                'ordering': ('name',),
                'verbose_name_plural': 'Degrees',
            },
        ),
        migrations.CreateModel(
            name='Fellowship',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('slug', autoslug.fields.AutoSlugField(unique=True, editable=False)),
            ],
            options={
                'ordering': ('name',),
                'verbose_name_plural': 'Fellowships',
            },
        ),
        migrations.CreateModel(
            name='Practitioner',
            fields=[
                ('docorsuser_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('physician_type', models.CharField(max_length=1, null=True, choices=[(b'0', b'General Physician'), (b'1', b'Trainee'), (b'2', b'Specialist')])),
                ('photo', sorl.thumbnail.fields.ImageField(null=True, upload_to=b'practitioner/', blank=True)),
                ('experience', models.PositiveIntegerField(help_text=b'Number of years')),
                ('achievements', models.TextField(null=True, blank=True)),
                ('message', models.CharField(max_length=140, null=True, blank=True)),
                ('slug', autoslug.fields.AutoSlugField(unique=True, editable=False)),
                ('status', models.BooleanField(default=False)),
                ('education_marks', models.PositiveIntegerField(default=0)),
                ('recommendation', models.PositiveIntegerField(default=0)),
                ('not_recommended', models.PositiveIntegerField(default=0)),
                ('review_rating', models.DecimalField(default=0.0, max_digits=2, decimal_places=2)),
                ('conditions', models.ManyToManyField(to='practitioner.Condition', blank=True)),
                ('degrees', models.ManyToManyField(to='practitioner.Degree')),
                ('fellowship', models.ManyToManyField(to='practitioner.Fellowship', blank=True)),
            ],
            options={
                'ordering': ('full_name',),
                'verbose_name_plural': 'Practitioners',
            },
            bases=('docorsauth.docorsuser',),
        ),
        migrations.CreateModel(
            name='Procedure',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('slug', autoslug.fields.AutoSlugField(unique=True, editable=False)),
            ],
            options={
                'ordering': ('name',),
                'verbose_name_plural': 'Procedures',
            },
        ),
        migrations.CreateModel(
            name='Specialization',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('human_name', models.CharField(max_length=100, null=True)),
                ('SEO_name', models.CharField(max_length=100, null=True)),
                ('slug', autoslug.fields.AutoSlugField(unique=True, editable=False)),
            ],
            options={
                'ordering': ('name',),
                'verbose_name_plural': 'Specialities',
            },
        ),
        migrations.AddField(
            model_name='procedure',
            name='specialization',
            field=models.ForeignKey(to='practitioner.Specialization'),
        ),
        migrations.AddField(
            model_name='practitioner',
            name='procedures',
            field=models.ManyToManyField(to='practitioner.Procedure', blank=True),
        ),
        migrations.AddField(
            model_name='practitioner',
            name='specialty',
            field=models.ForeignKey(blank=True, to='practitioner.Specialization', null=True),
        ),
        migrations.AddField(
            model_name='fellowship',
            name='specialization',
            field=models.ForeignKey(to='practitioner.Specialization'),
        ),
        migrations.AddField(
            model_name='condition',
            name='specialization',
            field=models.ForeignKey(to='practitioner.Specialization'),
        ),
    ]
