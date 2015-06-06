# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('date', models.DateTimeField(max_length=200)),
                ('resource', models.CharField(max_length=200)),
                ('read', models.BooleanField()),
                ('img', models.ImageField(upload_to=b'')),
            ],
        ),
    ]
