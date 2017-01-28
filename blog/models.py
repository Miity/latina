from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

class Post(models.Model):

    class Meta():
        db_table = 'posts'

    post_author = models.ForeignKey('auth.User')
    post_title = models.CharField(max_length=200)
    post_photo = models.ImageField(
        upload_to='blog_titels/',
        blank=True,
        null=True,
    )
    post_text = RichTextUploadingField()
    post_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.post_title