# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proceedings', '0005_auto_20160323_1335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poster',
            name='chair',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
    ]
