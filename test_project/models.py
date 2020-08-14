from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=30)
    cover = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title
