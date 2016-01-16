# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('request', '0017_auto_20160116_1730'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='copyright',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='explanation',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='title',
            field=models.CharField(max_length=150, blank=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='url',
            field=models.URLField(null=True, blank=True),
        ),
    ]
