# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-22 16:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginsignup', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='donor',
            name='email_confirmed',
            field=models.BooleanField(default=False),
        ),
    ]