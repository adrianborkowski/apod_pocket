# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('url', models.URLField()),
                ('media_type', models.CharField(max_length=5, choices=[('image', 'Image'), ('video', 'Video')])),
                ('explanation', models.TextField()),
                ('concepts', models.CharField(max_length=100)),
                ('date', models.DateField(max_length=50)),
            ],
        ),
    ]
