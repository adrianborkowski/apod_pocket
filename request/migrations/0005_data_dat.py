# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('request', '0004_auto_20151018_1850'),
    ]

    operations = [
        migrations.AddField(
            model_name='data',
            name='dat',
            field=models.DateField(default=datetime.datetime(2015, 10, 18, 17, 0, 26, 35784, tzinfo=utc)),
        ),
    ]
