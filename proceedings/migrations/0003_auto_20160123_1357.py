# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proceedings', '0002_session_chair'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session',
            name='session',
            field=models.CharField(max_length=20),
        ),
    ]
