# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-08-31 18:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0012_auto_20170831_1642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='checkout.Order'),
        ),
    ]