# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-24 21:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0002_remove_joinuser_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='joinuser',
            name='trip',
        ),
        migrations.DeleteModel(
            name='JoinUser',
        ),
    ]
