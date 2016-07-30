# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('request', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='data',
            name='date',
        ),
        migrations.AlterField(
            model_name='data',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
