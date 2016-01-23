# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('committee', '0003_auto_20150703_2007'),
        ('proceedings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='session',
            name='chair',
            field=models.ForeignKey(blank=True, to='committee.Member', null=True),
            preserve_default=True,
        ),
    ]
