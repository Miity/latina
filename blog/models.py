from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    published_date = models.DateTimeField(blank=True, null=True)
    photo = models.ImageField(
        upload_to='static/images/',
        blank=True,
        null=True,
    )

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title