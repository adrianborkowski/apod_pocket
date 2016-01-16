# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('request', '0016_auto_20160116_1430'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='data',
            name='concepts',
        ),
        migrations.AddField(
            model_name='data',
            name='copyright',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
