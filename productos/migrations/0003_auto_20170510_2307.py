# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-11 04:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0002_auto_20170510_2302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venta',
            name='valor',
            field=models.IntegerField(),
        ),
    ]
