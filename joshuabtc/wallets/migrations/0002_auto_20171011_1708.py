# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-10-11 17:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wallets', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='btc',
            name='address',
        ),
        migrations.RemoveField(
            model_name='btc',
            name='invoice',
        ),
        migrations.RemoveField(
            model_name='btc',
            name='payment_code',
        ),
        migrations.RemoveField(
            model_name='eth',
            name='address',
        ),
        migrations.RemoveField(
            model_name='eth',
            name='private',
        ),
        migrations.RemoveField(
            model_name='eth',
            name='public',
        ),
    ]
