# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('skills', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='description',
            field=models.TextField(default=b'Skill Description'),
        ),
        migrations.AlterField(
            model_name='entry',
            name='img',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
    ]
