from django.db import models


class Post(models.Model):
    url = models.CharField(max_length=300, blank=True)
    files = models.FileField(upload_to='', blank=True)

    width = models.CharField(max_length=300, default='width')
    height = models.CharField(max_length=300, default='height')
