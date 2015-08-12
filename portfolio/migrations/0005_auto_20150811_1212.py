# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0004_auto_20150712_0716'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='description',
            field=models.TextField(default='Project description'),
        ),
        migrations.AlterField(
            model_name='entry',
            name='img',
            field=models.ImageField(null=True, blank=True, upload_to=''),
        ),
    ]
