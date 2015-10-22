# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('request', '0009_auto_20151018_1944'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='data',
            name='date_created',
        ),
    ]
