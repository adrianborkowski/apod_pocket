# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('request', '0005_data_dat'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='data',
            name='dat',
        ),
        migrations.AddField(
            model_name='data',
            name='date_created',
            field=models.DateField(default=datetime.datetime(2015, 10, 18, 17, 4, 54, 822490, tzinfo=utc)),
        ),
    ]
