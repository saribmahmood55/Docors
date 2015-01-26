# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('practice', '0004_auto_20150123_1508'),
    ]

    operations = [
        migrations.AlterField(
            model_name='practicetiming',
            name='day',
            field=models.CharField(help_text=b'Select Day.', max_length=1, choices=[(b'1', b'Monday'), (b'2', b'Tuesday'), (b'3', b'Wednesday'), (b'4', b'Thursday'), (b'5', b'Friday'), (b'6', b'Saturday'), (b'7', b'Sunday')]),
        ),
        migrations.AlterField(
            model_name='practicetiming',
            name='end_time',
            field=models.CharField(help_text=b'Select ending Time for Clininc.', max_length=2, choices=[(b'0', b'07:00am'), (b'1', b'07:30am'), (b'2', b'08:00am'), (b'3', b'08:30am'), (b'4', b'09:00am'), (b'5', b'09:30am'), (b'6', b'10:00am'), (b'7', b'10:30am'), (b'8', b'11:00am'), (b'9', b'11:30am'), (b'10', b'12:00pm'), (b'11', b'12:30pm'), (b'12', b'01:00pm'), (b'13', b'01:30pm'), (b'14', b'02:00pm'), (b'15', b'02:30am'), (b'16', b'03:00pm'), (b'17', b'03:30pm'), (b'18', b'04:00pm'), (b'19', b'04:30pm'), (b'20', b'05:00pm'), (b'21', b'05:30pm'), (b'22', b'06:00pm'), (b'23', b'06:30pm'), (b'24', b'07:00pm'), (b'25', b'07:30pm'), (b'26', b'08:00pm'), (b'27', b'08:30pm'), (b'28', b'09:00pm'), (b'29', b'09:30pm'), (b'30', b'10:00pm'), (b'31', b'10:30pm'), (b'32', b'11:00pm'), (b'33', b'11:30pm'), (b'34', b'12:00am'), (b'35', b'12:30am'), (b'36', b'01:00am'), (b'37', b'02:00am'), (b'38', b'02:30am')]),
        ),
        migrations.AlterField(
            model_name='practicetiming',
            name='start_time',
            field=models.CharField(help_text=b'Select starting Time for Clininc.', max_length=2, choices=[(b'0', b'07:00am'), (b'1', b'07:30am'), (b'2', b'08:00am'), (b'3', b'08:30am'), (b'4', b'09:00am'), (b'5', b'09:30am'), (b'6', b'10:00am'), (b'7', b'10:30am'), (b'8', b'11:00am'), (b'9', b'11:30am'), (b'10', b'12:00pm'), (b'11', b'12:30pm'), (b'12', b'01:00pm'), (b'13', b'01:30pm'), (b'14', b'02:00pm'), (b'15', b'02:30am'), (b'16', b'03:00pm'), (b'17', b'03:30pm'), (b'18', b'04:00pm'), (b'19', b'04:30pm'), (b'20', b'05:00pm'), (b'21', b'05:30pm'), (b'22', b'06:00pm'), (b'23', b'06:30pm'), (b'24', b'07:00pm'), (b'25', b'07:30pm'), (b'26', b'08:00pm'), (b'27', b'08:30pm'), (b'28', b'09:00pm'), (b'29', b'09:30pm'), (b'30', b'10:00pm'), (b'31', b'10:30pm'), (b'32', b'11:00pm'), (b'33', b'11:30pm'), (b'34', b'12:00am'), (b'35', b'12:30am'), (b'36', b'01:00am'), (b'37', b'02:00am'), (b'38', b'02:30am')]),
        ),
    ]
