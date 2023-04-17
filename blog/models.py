from django.db import models
from django.utils import timezone


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
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2,
                              choices=Status.choices,
                              default=Status.DRAFT)

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


