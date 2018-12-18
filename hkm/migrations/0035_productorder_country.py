# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-12-12 14:02
from __future__ import unicode_literals

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('hkm', '0034_postal_code_to_charfield'),
    ]

    operations = [
        migrations.AddField(
            model_name='productorder',
            name='country',
            field=django_countries.fields.CountryField(default='FI', max_length=2, verbose_name='Country'),
        ),
    ]
