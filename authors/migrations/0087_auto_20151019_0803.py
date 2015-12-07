# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0086_merge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='abstract',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 19, 8, 3, 8, 861628)),
        ),
        migrations.AlterField(
            model_name='abstract',
            name='delivery_decision',
            field=models.CharField(default=b'Oral', choices=[(b'Oral', b'Oral'), (b'Poster', b'Poster')], max_length=6, blank=True, null=True, verbose_name=b'Decision'),
        ),
    ]
