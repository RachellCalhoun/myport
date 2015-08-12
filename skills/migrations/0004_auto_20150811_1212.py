# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('skills', '0003_auto_20150712_0750'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='date',
            field=models.DateTimeField(verbose_name='date published', blank=True, default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='entry',
            name='description',
            field=models.TextField(default='Skill Description'),
        ),
        migrations.AlterField(
            model_name='entry',
            name='img',
            field=models.ImageField(null=True, blank=True, upload_to=''),
        ),
    ]
