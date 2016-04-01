# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0126_merge'),
    ]

    operations = [
        migrations.AddField(
            model_name='abstract',
            name='poster_file',
            field=models.FileField(help_text=b'Please submit A4 .pdf, max size 5MB', null=True, upload_to=b'posters', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='abstract',
            name='poster_link',
            field=models.URLField(help_text=b'e.g. http://dropbox ...', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='abstract',
            name='slides_files',
            field=models.FileField(help_text=b'Please submit .pdf only, max size 5MB', null=True, upload_to=b'slides', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='abstract',
            name='slides_link',
            field=models.URLField(help_text=b'e.g. http://dropbox ...', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='abstract',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 1, 13, 33, 46, 934995)),
        ),
    ]
