# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proceedings', '0004_poster'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session',
            name='chair',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
    ]
