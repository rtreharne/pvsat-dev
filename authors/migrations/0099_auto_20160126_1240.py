# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0098_auto_20160123_1539'),
    ]

    operations = [
        migrations.AlterField(
            model_name='abstract',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 26, 12, 40, 54, 941962)),
        ),
        migrations.AlterField(
            model_name='abstract',
            name='upload',
            field=models.FileField(null=True, upload_to=b'abstract_uploads', blank=True),
        ),
    ]
