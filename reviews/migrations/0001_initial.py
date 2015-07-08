# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0001_initial'),
        ('practitioner', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('answer1', models.PositiveIntegerField(default=0)),
                ('answer2', models.PositiveIntegerField(default=0)),
                ('answer3', models.PositiveIntegerField(default=0)),
                ('answer4', models.PositiveIntegerField(default=0)),
                ('answer5', models.PositiveIntegerField(default=0)),
            ],
            options={
                'verbose_name_plural': 'Answers',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.CharField(max_length=150)),
                ('agree', models.PositiveIntegerField(default=0)),
                ('disagree', models.PositiveIntegerField(default=0)),
            ],
            options={
                'verbose_name_plural': 'Comments',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('question1', models.CharField(max_length=150)),
                ('question2', models.CharField(max_length=150)),
                ('question3', models.CharField(max_length=150)),
                ('question4', models.CharField(max_length=150)),
                ('question5', models.CharField(max_length=150)),
            ],
            options={
                'verbose_name_plural': 'Questions',
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('anonymous', models.NullBooleanField()),
                ('timestamp', models.DateTimeField(auto_now=True, null=True)),
                ('answers', models.ForeignKey(to='reviews.Answer', null=True)),
                ('comments', models.ForeignKey(to='reviews.Comment', null=True)),
                ('patient', models.ForeignKey(to='patients.Patient')),
                ('practitioner', models.ForeignKey(to='practitioner.Practitioner')),
            ],
            options={
                'verbose_name_plural': 'Reviews',
            },
        ),
    ]
