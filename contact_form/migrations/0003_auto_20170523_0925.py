# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-23 03:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact_form', '0002_auto_20170522_1316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='details',
            name='date',
            field=models.DateTimeField(null=True),
        ),
    ]
