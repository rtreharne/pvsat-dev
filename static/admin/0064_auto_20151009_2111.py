# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import sorl.thumbnail.fields
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0063_auto_20151009_2038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='abstract',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 9, 21, 11, 7, 398155)),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='picture',
            field=sorl.thumbnail.fields.ImageField(null=True, upload_to=b'user_images', blank=True),
        ),
    ]
