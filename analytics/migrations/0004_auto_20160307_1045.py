# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-07 10:45
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('analytics', '0003_auto_20160307_1038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pageview',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2016, 3, 7, 10, 45, 32, 701299, tzinfo=utc)),
        ),
    ]
