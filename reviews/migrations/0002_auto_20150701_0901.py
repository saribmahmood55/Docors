# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
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
        migrations.RemoveField(
            model_name='recommendations',
            name='patient',
        ),
        migrations.RemoveField(
            model_name='recommendations',
            name='practitioner',
        ),
        migrations.RemoveField(
            model_name='reviewstats',
            name='patient',
        ),
        migrations.RemoveField(
            model_name='reviewstats',
            name='review',
        ),
        migrations.RemoveField(
            model_name='review',
            name='down_votes',
        ),
        migrations.RemoveField(
            model_name='review',
            name='post_as_anonymous',
        ),
        migrations.RemoveField(
            model_name='review',
            name='review_date',
        ),
        migrations.RemoveField(
            model_name='review',
            name='review_text',
        ),
        migrations.RemoveField(
            model_name='review',
            name='up_votes',
        ),
        migrations.AddField(
            model_name='review',
            name='anonymous',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='review',
            name='timestamp',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.DeleteModel(
            name='Recommendations',
        ),
        migrations.DeleteModel(
            name='ReviewStats',
        ),
        migrations.AddField(
            model_name='review',
            name='answers',
            field=models.ForeignKey(to='reviews.Answer', null=True),
        ),
        migrations.AddField(
            model_name='review',
            name='comments',
            field=models.ForeignKey(to='reviews.Comment', null=True),
        ),
    ]
