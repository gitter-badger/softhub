# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-04-08 15:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('softhub', '0011_auto_20170404_1605'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='website',
            field=models.URLField(default='http://www.duckduckgo.com'),
            preserve_default=False,
        ),
    ]
