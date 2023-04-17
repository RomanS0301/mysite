from django.db import models
from django.utils import timezone

from django.contrib.auth.models import User


class Post(models.Model):
    class Status(models.TextChoices):
        """
        Добавление поля статуса, которое позволит управлять статусом постов блога. В постах будет использоваться статусы
        Draft(черновик) и Published(опубликован)
        """
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'

    title = models.CharField(max_length=250, verbose_name='Заголовок')
    slug = models.SlugField(max_length=250, verbose_name='Слаг')
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='blog_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now, verbose_name='Дата публикации')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата сосздания')
    update = models.DateTimeField(auto_now=True, verbose_name='Дата редактирования')
    status = models.CharField(max_length=2,
                              choices=Status.choices,
                              default=Status.DRAFT,
                              verbose_name="Статус")

    class Meta:
        """
        Определение предустановленного порядка сортировки
        """
        ordering = ['-publish']
        # Добавление индекса модели
        indexes = [
            models.Index(fields=['-publish']),
        ]

    def __str__(self):
        return self.title


