from django.db import models


class Post(models.Model):
    url = models.CharField(max_length=300)
    files = models.FileField(upload_to='uploads/%Y/%m/%d/')

    def __str__(self):
        return self.title
