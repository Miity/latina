# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-15 08:54
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20170213_2044'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post_short_description',
            field=ckeditor.fields.RichTextField(blank=True, max_length=300, null=True, verbose_name='Короткое описание'),
        ),
    ]
