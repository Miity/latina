# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-21 19:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='static/images/'),
        ),
    ]
