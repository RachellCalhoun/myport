# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_auto_20150712_0626'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='date',
            field=models.DateTimeField(max_length=200, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='entry',
            name='description',
            field=models.TextField(default=b'Project description'),
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
