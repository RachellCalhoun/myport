# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20150606_1220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='date',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name=b'date published', blank=True),
        ),
        migrations.AlterField(
            model_name='entry',
            name='img',
            field=models.ImageField(null=True, upload_to=b'', blank=True),
        ),
        migrations.AlterField(
            model_name='entry',
            name='resource',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
    ]
