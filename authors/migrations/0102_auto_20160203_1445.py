# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0101_auto_20160203_1414'),
    ]

    operations = [
        migrations.AlterField(
            model_name='abstract',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2016, 2, 3, 14, 45, 24, 16548)),
        ),
        migrations.AlterField(
            model_name='abstract',
            name='poster_id',
            field=models.CharField(max_length=11, null=True, blank=True),
        ),
    ]
