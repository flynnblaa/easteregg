# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-03-20 04:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('egghunt', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='egg',
            old_name='radius',
            new_name='radius_in_metres',
        ),
    ]