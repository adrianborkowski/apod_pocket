# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('request', '0012_auto_20151018_2106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='created_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
