# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import authors.models


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0120_auto_20160214_0752'),
    ]

    operations = [
        migrations.AlterField(
            model_name='abstract',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2016, 2, 14, 8, 1, 25, 55044)),
        ),
        migrations.AlterField(
            model_name='abstract',
            name='paper',
            field=models.FileField(blank=True, null=True, upload_to=b'abstract_uploads', validators=[authors.models.validate_paper_ext]),
        ),
    ]
