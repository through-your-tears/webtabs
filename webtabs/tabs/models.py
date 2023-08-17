from django.conf import settings
from django.db import models

# Create your models here.


class Collection(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)


class WebTag(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField(null=True)
    url = models.URLField()
    url_type = models.CharField(max_length=8, default='website', choices=(
        ('website', 'website'),
        ('book', 'book'),
        ('article', 'article'),
        ('music', 'music'),
        ('video', 'video'),
    ))
    image = models.ImageField(upload_to='images/', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    collection = models.ForeignKey(Collection, on_delete=models.SET_NULL, null=True, default=None)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
