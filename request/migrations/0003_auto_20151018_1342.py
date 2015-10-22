# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('request', '0002_auto_20151018_1255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='concepts',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='data',
            name='media_type',
            field=models.CharField(choices=[('image', 'Image'), ('video', 'Video')], max_length=10),
        ),
        migrations.AlterField(
            model_name='data',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]
