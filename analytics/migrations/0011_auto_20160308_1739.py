# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-08 17:39
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('analytics', '0010_auto_20160308_1738'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pageview',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2016, 3, 8, 17, 39, 53, 281940, tzinfo=utc)),
        ),
    ]
