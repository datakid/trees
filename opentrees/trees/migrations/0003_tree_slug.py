# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('trees', '0002_auto_20150407_1037'),
    ]

    operations = [
        migrations.AddField(
            model_name='tree',
            name='slug',
            field=models.SlugField(default=datetime.datetime(2015, 4, 7, 10, 43, 46, 729885, tzinfo=utc), unique=True, max_length=60),
            preserve_default=False,
        ),
    ]
