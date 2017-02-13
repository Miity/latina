from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse


# Create your models here.


# Модель категории
class Category(models.Model):

    name = models.CharField(max_length=50, unique=True, verbose_name="Название")
    slug = models.SlugField(max_length=200, db_index=True, unique=True, verbose_name="URL-название")

    def get_absolute_url(self):
        return reverse('blog:BlogListByCategory', args=[self.slug])

    class Meta():
        db_table = 'category'
        ordering = ['name']
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Post(models.Model):
    post_category = models.ForeignKey(Category, related_name='post', verbose_name="Категория")
    post_title = models.CharField(max_length=200, db_index=True, verbose_name="Название")
    post_slug = models.SlugField(max_length=200, db_index=True, verbose_name="URL-название")
    post_img = models.ImageField(upload_to='blog_titels/', blank=True, null=True, verbose_name="Изображение")
    post_description = RichTextField(blank=True, verbose_name="Описание")
    post_available = models.BooleanField(default=True, verbose_name="Доступно/нет")
    post_created = models.DateTimeField(auto_now_add=True, verbose_name="Дата публикации")
    post_updated = models.DateTimeField(auto_now=True, verbose_name="Дата последнего обновления")

    def get_absolute_url(self):
        return reverse('blog:PostDetail', args=[self.id, self.post_slug])

    class Meta():
        db_table = 'posts'
        index_together = ['id', 'post_slug']
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
    def __str__(self):
        return self.post_title

    def bit(self):
        if self.post_photo:
            return u'<img src="/media/{}" width="100px"/>'.format(self.post_img)
        else:
            return u'(none)'
    bit.short_description = u'Изображение'
    bit.allow_tags = True


class Comments (models.Model):
    class Meta():
        db_table = 'comments'

    comments_date = models.DateTimeField(blank=True, null=True, )
    comments_text = models.TextField(verbose_name="Комментарии")
    comments_post = models.ForeignKey(Post)
    comments_user = models.ForeignKey(User)