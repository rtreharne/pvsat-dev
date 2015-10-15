# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('programme', '0002_theme'),
    ]

    operations = [
        migrations.AlterField(
            model_name='speaker',
            name='forename',
            field=models.CharField(max_length=128),
        ),
    ]
