# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import authors.models


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0105_auto_20160214_0647'),
    ]

    operations = [
        migrations.AlterField(
            model_name='abstract',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2016, 2, 14, 7, 17, 30, 885947)),
        ),
        migrations.AlterField(
            model_name='abstract',
            name='upload',
            field=models.FileField(upload_to=b'abstract_uploads', validators=[authors.models.validate_file_extension]),
        ),
    ]
