# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-04-11 10:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hkm', '0018_auto_20170411_1301'),
    ]

    operations = [
        migrations.AddField(
            model_name='productorder',
            name='total_price_with_postage',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Total price with postage'),
        ),
    ]
