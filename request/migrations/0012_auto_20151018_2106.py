# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('request', '0011_data_created_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='url',
            field=models.URLField(verbose_name=''),
        ),
    ]
