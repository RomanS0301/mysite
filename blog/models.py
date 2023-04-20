from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# https://docs.djangoproject.com/en/4.1/ref/urlresolvers/#reverse
from django.urls import reverse


class PublishedManager(models.Manager):
    """
    Создание конкретно-прикладного менеджера
    """
    def get_queryset(self):
        return super().get_queryset()\
            .filter(status=Post.Status.PUBLISHED)


class Post(models.Model):
    class Status(models.TextChoices):
        """
        Добавление поля статуса, которое позволит управлять статусом постов блога. В постах будет использоваться статусы
        Draft(черновик) и Published(опубликован)
        """
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'

    title = models.CharField(max_length=250, verbose_name='Заголовок')
    slug = models.SlugField(max_length=250, unique_for_date='publish', verbose_name='Слаг')
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='blog_posts',
                               verbose_name='Автор')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now, verbose_name='Дата публикации')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    update = models.DateTimeField(auto_now=True, verbose_name='Дата редактирования')
    status = models.CharField(max_length=2,
                              choices=Status.choices,
                              default=Status.DRAFT,
                              verbose_name="Статус")

    objects = models.Manager()  # менеджер, применяемый по умолчанию
    published = PublishedManager()  # конкретно-прикладной менеджер

    class Meta:
        # Определение предустановленного порядка сортировки
        ordering = ['-publish']
        # Добавление индекса модели
        indexes = [
            models.Index(fields=['-publish']),
        ]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail',
                       args=[self.publish.year,
                             self.publish.month,
                             self.publish.day,
                             self.slug])


class Comment(models.Model):
    post = models.ForeignKey(Post,
                             on_delete=models.CASCADE,
                             related_name='comments')  # позволяет назначить имя атрибуту для связи
    # ассоциированого объекта назад к нему
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)  # все комментарии по умолчанию активны

    class Meta:
        ordering = ['created']
        indexes = [
            models.Index(fields=['created']),
        ]

    def __str__(self):
        return f'Комментарий {self.name} {self.post}'
