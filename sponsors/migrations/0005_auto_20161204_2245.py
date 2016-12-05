# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sponsors', '0004_sponsor_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sponsor',
            name='type',
            field=models.CharField(default=99, max_length=129, choices=[(b'99', b'-'), (b'Main', b'Main'), (b'Associate', b'Associate'), (b'Poster', b'Poster')]),
        ),
        migrations.DeleteModel(
            name='SponsorType',
        ),
    ]
