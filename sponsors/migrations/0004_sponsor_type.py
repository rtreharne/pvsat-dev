# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sponsors', '0003_sponsortype'),
    ]

    operations = [
        migrations.AddField(
            model_name='sponsor',
            name='type',
            field=models.ForeignKey(default=99, to='sponsors.SponsorType'),
            preserve_default=False,
        ),
    ]
