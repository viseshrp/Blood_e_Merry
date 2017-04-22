# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-22 19:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginsignup', '0002_donor_email_confirmed'),
    ]

    operations = [
        migrations.AddField(
            model_name='donor',
            name='blood_group',
            field=models.CharField(default='', max_length=2),
        ),
        migrations.AlterField(
            model_name='donor',
            name='city',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='donor',
            name='state',
            field=models.CharField(default='', max_length=30),
        ),
    ]
