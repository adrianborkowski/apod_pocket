# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('request', '0010_remove_data_date_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='data',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
