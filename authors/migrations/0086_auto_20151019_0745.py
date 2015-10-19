# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0085_auto_20151017_1200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='abstract',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 19, 7, 45, 38, 556586)),
        ),
        migrations.AlterField(
            model_name='abstract',
            name='delivery_decision',
            field=models.CharField(default=b'Oral', choices=[(b'Oral', b'Oral'), (b'Poster', b'Poster')], max_length=6, blank=True, null=True, verbose_name=b'Decision'),
        ),
    ]
