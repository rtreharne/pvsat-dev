# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sponsors', '0002_sponsor_logo'),
    ]

    operations = [
        migrations.CreateModel(
            name='SponsorType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.CharField(default=99, max_length=129, choices=[(b'99', b'-'), (b'Main', b'Main'), (b'Associate', b'Associate'), (b'Poster', b'Poster')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
