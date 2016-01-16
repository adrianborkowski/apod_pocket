# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('request', '0015_auto_20151026_1907'),
    ]

    operations = [
        migrations.RenameField(
            model_name='data',
            old_name='created_date',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='data',
            old_name='media_type',
            new_name='type',
        ),
    ]
