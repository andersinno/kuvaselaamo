# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-12-13 10:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hkm', '0031_no_shipment_fee_discount'),
    ]

    operations = [
        migrations.AddField(
            model_name='campaigncode',
            name='use_type',
            field=models.CharField(choices=[(b'SINGLE_USE', 'Kertak\xe4ytt\xf6inen'), (b'MULTI_USE', 'Monik\xe4ytt\xf6inen')], db_index=True, default=b'SINGLE_USE', max_length=20, verbose_name='K\xe4ytt\xf6'),
        ),
    ]