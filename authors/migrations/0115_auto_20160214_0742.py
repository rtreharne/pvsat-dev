# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0114_auto_20160214_0730'),
    ]

    operations = [
        migrations.AlterField(
            model_name='abstract',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2016, 2, 14, 7, 42, 27, 274200)),
        ),
        migrations.AlterField(
            model_name='abstract',
            name='paper',
            field=models.FileField(null=True, upload_to=b'abstract_uploads', blank=True),
        ),
    ]
