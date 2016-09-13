# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-17 10:41
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0008_auto_20160317_1040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membership',
            name='date_end',
            field=models.DateTimeField(default=datetime.datetime(2016, 3, 17, 10, 41, 1, 736968, tzinfo=utc), verbose_name='End Date'),
        ),
        migrations.AlterField(
            model_name='membership',
            name='date_start',
            field=models.DateTimeField(default=datetime.datetime(2016, 3, 17, 10, 41, 1, 736912, tzinfo=utc), verbose_name='Start Date'),
        ),
    ]