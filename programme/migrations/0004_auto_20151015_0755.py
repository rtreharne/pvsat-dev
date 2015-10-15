# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('programme', '0003_auto_20151015_0737'),
    ]

    operations = [
        migrations.AlterField(
            model_name='speaker',
            name='surname',
            field=models.CharField(max_length=128),
        ),
    ]
