# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import authors.models


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0097_auto_20160123_1357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='abstract',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 23, 15, 39, 45, 817044)),
        ),
        migrations.AlterField(
            model_name='abstract',
            name='upload',
            field=models.FileField(blank=True, null=True, upload_to=b'abstract_uploads', validators=[authors.models.validate_file_extension]),
        ),
    ]
