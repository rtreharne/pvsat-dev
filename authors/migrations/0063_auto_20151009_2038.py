# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0062_auto_20151007_1440'),
    ]

    operations = [
        migrations.AlterField(
            model_name='abstract',
            name='abstract',
            field=models.TextField(max_length=50000, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='abstract',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 9, 20, 38, 54, 517503)),
        ),
    ]
