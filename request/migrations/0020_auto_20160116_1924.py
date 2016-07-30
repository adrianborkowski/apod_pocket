# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('request', '0019_auto_20160116_1922'),
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
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='title',
            field=models.CharField(max_length=150, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='type',
            field=models.CharField(choices=[('image', 'Image'), ('video', 'Video')], null=True, max_length=10, blank=True),
        ),
    ]
