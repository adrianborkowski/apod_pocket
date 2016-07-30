# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('request', '0014_auto_20151022_2239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='created_date',
            field=models.DateField(null=True, blank=True),
        ),
    ]
