# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0070_auto_20151010_0707'),
    ]

    operations = [
        migrations.AlterField(
            model_name='abstract',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 10, 7, 8, 25, 112410)),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='url',
            field=models.URLField(help_text=b'http://mygroupwebsite.com', blank=True),
        ),
    ]
