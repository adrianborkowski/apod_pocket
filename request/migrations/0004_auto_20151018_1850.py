# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('request', '0003_auto_20151018_1342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='title',
            field=models.CharField(max_length=10),
        ),
    ]
