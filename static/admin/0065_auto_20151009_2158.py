# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0064_auto_20151009_2111'),
    ]

    operations = [
        migrations.AddField(
            model_name='abstract',
            name='authors',
            field=models.CharField(default='R. E. Treharne', help_text=b'e.g. J. Bloggs, M. C. Hammer ...', max_length=500),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='abstract',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 9, 21, 57, 58, 956738)),
        ),
    ]
