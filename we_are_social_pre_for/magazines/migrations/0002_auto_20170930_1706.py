# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-30 17:06
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('magazines', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='subscription_end',
            field=models.DateTimeField(default=datetime.datetime(2017, 9, 30, 17, 6, 43, 151201, tzinfo=utc)),
        ),
    ]