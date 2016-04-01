# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0127_auto_20160401_1333'),
    ]

    operations = [
        migrations.RenameField(
            model_name='abstract',
            old_name='slides_files',
            new_name='slides_file',
        ),
        migrations.AlterField(
            model_name='abstract',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 1, 14, 3, 3, 146156)),
        ),
    ]
