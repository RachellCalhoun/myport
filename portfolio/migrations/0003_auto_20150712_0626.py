# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_auto_20150606_1220'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entry',
            name='read',
        ),
        migrations.AddField(
            model_name='entry',
            name='description',
            field=models.TextField(default=b'Project Desciption'),
        ),
    ]
