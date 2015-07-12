# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('date', models.DateTimeField(default=datetime.datetime.now, verbose_name=b'date published', blank=True)),
                ('description', models.TextField()),
                ('resource', models.CharField(max_length=200, null=True, blank=True)),
                ('img', models.ImageField(null=True, upload_to=b'', blank=True)),
            ],
        ),
    ]
