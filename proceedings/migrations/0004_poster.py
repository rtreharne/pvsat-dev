# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('committee', '0003_auto_20150703_2007'),
        ('proceedings', '0003_auto_20160123_1357'),
    ]

    operations = [
        migrations.CreateModel(
            name='Poster',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('session', models.CharField(max_length=20)),
                ('start', models.DateTimeField()),
                ('finish', models.DateTimeField()),
                ('chair', models.ForeignKey(blank=True, to='committee.Member', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
