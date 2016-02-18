# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0121_auto_20160214_0801'),
    ]

    operations = [
        migrations.AlterField(
            model_name='abstract',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2016, 2, 18, 16, 11, 25, 986959)),
        ),
        migrations.AlterField(
            model_name='abstract',
            name='paper',
            field=models.FileField(null=True, upload_to=b'abstract_uploads', blank=True),
        ),
    ]
