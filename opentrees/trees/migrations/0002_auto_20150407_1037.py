# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trees', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tree',
            name='crown',
            field=models.IntegerField(null=True, verbose_name=b'Width in metres of foliage', blank=True),
        ),
    ]
