# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0119_auto_20160214_0749'),
    ]

    operations = [
        migrations.AlterField(
            model_name='abstract',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2016, 2, 14, 7, 52, 39, 869096)),
        ),
        migrations.AlterField(
            model_name='abstract',
            name='unique_id',
            field=models.CharField(max_length=11, unique=True, null=True),
        ),
    ]
