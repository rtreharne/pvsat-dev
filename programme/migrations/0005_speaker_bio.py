# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('programme', '0004_auto_20151015_0755'),
    ]

    operations = [
        migrations.AddField(
            model_name='speaker',
            name='bio',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
