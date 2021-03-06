# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-17 08:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_post_post_short_description'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-post_created'], 'verbose_name': 'Пост', 'verbose_name_plural': 'Посты'},
        ),
        migrations.AlterField(
            model_name='post',
            name='post_created',
            field=models.DateField(auto_now_add=True, verbose_name='Дата публикации'),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_updated',
            field=models.DateField(auto_now=True, verbose_name='Последние обновления'),
        ),
    ]
