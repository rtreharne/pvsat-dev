# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0075_auto_20151012_1221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='abstract',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 12, 18, 26, 25, 649753)),
        ),
        migrations.AlterField(
            model_name='abstract',
            name='delivery',
            field=models.CharField(default=b'Oral', help_text=b'N.B. We require that a paper be submitted for each abstract - even if you request a poster presentation.', max_length=6, choices=[(b'Oral', b'Oral'), (b'Poster', b'Poster')]),
        ),
    ]
