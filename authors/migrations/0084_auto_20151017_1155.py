# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0083_auto_20151017_0628'),
    ]

    operations = [
        migrations.AddField(
            model_name='abstract',
            name='delivery_decision',
            field=models.CharField(default=b'Oral', max_length=6, null=True, blank=True, choices=[(b'Oral', b'Oral'), (b'Poster', b'Poster')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='abstract',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 17, 11, 55, 2, 381342)),
        ),
    ]
