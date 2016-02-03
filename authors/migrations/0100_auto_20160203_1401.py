# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0099_auto_20160126_1240'),
    ]

    operations = [
        migrations.AddField(
            model_name='abstract',
            name='poster_id',
            field=models.CharField(max_length=11, unique=True, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='abstract',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2016, 2, 3, 14, 1, 10, 971589)),
        ),
    ]
