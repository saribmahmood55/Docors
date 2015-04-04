# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import sorl.thumbnail.fields
import autoslug.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
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
                'verbose_name_plural': 'Degrees',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Practitioner',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.PositiveSmallIntegerField(blank=True, null=True, choices=[(1, b'Dr. '), (2, b'Prof. '), (3, b'Prof. Dr. ')])),
                ('name', models.CharField(max_length=100)),
                ('gender', models.CharField(default=b'M', max_length=1, choices=[(b'M', b'Male'), (b'F', b'Female')])),
                ('year_of_birth', models.PositiveIntegerField(default=0)),
                ('photo', sorl.thumbnail.fields.ImageField(null=True, upload_to=b'practitioner/', blank=True)),
                ('email', models.EmailField(max_length=75, null=True, blank=True)),
                ('experience', models.PositiveIntegerField(help_text=b'Number of years')),
                ('physician_type', models.PositiveSmallIntegerField(blank=True, help_text=b'Physician type', null=True, choices=[(1, b'Trainee'), (2, b'Specialist')])),
                ('achievements', models.TextField(null=True, blank=True)),
                ('message', models.TextField(max_length=140, null=True, blank=True)),
                ('slug', autoslug.fields.AutoSlugField(unique=True, editable=False)),
                ('status', models.BooleanField(default=False)),
                ('education_marks', models.PositiveIntegerField(default=0)),
                ('recommendation', models.PositiveIntegerField(default=0)),
                ('not_recommended', models.PositiveIntegerField(default=0)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('degrees', models.ManyToManyField(to='practitioner.Degree')),
            ],
            options={
            },
            bases=(models.Model,),
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
                'verbose_name_plural': 'Specialities',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='practitioner',
            name='specialities',
            field=models.ManyToManyField(to='practitioner.Specialization'),
            preserve_default=True,
        ),
    ]
