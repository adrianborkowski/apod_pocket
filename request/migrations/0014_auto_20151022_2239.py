# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('request', '0013_auto_20151020_2218'),
    ]

    operations = [
        migrations.AddField(
            model_name='data',
            name='hd_url',
            field=models.URLField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='concepts',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='data',
            name='created_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='data',
            name='title',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='data',
            name='url',
            field=models.URLField(),
        ),
    ]
