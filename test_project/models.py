from django.db import models


class Post(models.Model):
    url = models.CharField(max_length=300, blank=True)
    files = models.FileField(upload_to='', blank=True)

    def __str__(self):
        return self.title