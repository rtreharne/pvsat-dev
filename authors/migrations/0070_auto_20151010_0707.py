# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0069_auto_20151010_0645'),
    ]

    operations = [
        migrations.AlterField(
            model_name='abstract',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 10, 7, 7, 42, 156821)),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='twitter',
            field=models.CharField(help_text=b'e.g. "@pvsat-12"', max_length=20, blank=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='url',
            field=models.URLField(help_text=b'http://google.com', blank=True),
        ),
    ]
