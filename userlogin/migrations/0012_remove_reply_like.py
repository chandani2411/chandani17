# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-01 12:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userlogin', '0011_auto_20160801_0710'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reply',
            name='like',
        ),
    ]