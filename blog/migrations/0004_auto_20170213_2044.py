# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-13 20:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20170213_1740'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name': 'Пост', 'verbose_name_plural': 'Посты'},
        ),
        migrations.RemoveField(
            model_name='post',
            name='post_photo',
        ),
        migrations.AddField(
            model_name='post',
            name='post_img',
            field=models.ImageField(blank=True, null=True, upload_to='blog_titels/', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=50, unique=True, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(max_length=200, unique=True, verbose_name='URL-название'),
        ),
        migrations.AlterField(
            model_name='comments',
            name='comments_text',
            field=models.TextField(verbose_name='Комментарии'),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_available',
            field=models.BooleanField(default=True, verbose_name='Доступно/нет'),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации'),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_slug',
            field=models.SlugField(max_length=200, verbose_name='URL-название'),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата последнего обновления'),
        ),
    ]