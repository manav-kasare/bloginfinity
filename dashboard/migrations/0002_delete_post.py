# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2020-03-27 13:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Post',
        ),
    ]
