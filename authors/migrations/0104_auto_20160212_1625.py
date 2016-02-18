# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0103_auto_20160203_2300'),
    ]

    operations = [
        migrations.AddField(
            model_name='abstract',
            name='paper',
            field=models.FileField(null=True, upload_to=b'abstract_uploads', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='abstract',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2016, 2, 12, 16, 25, 3, 949793)),
        ),
    ]
