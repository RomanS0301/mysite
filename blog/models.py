from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=250, verbose_name='Заголовок')
    slug = models.SlugField(max_length=250, verbose_name='Слаг')
    body = models.TextField()

    def __str__(self):
        return self.title


