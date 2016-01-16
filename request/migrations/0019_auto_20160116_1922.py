# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('request', '0018_auto_20160116_1852'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='copyright',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
    ]
