from django import template
from ..models import Post

# Создание конкретно-прикладных шаблонных тегов для выполнения конкретных задач

register = template.Library()


@register.simple_tag
def total_posts():
    """
    Создан шаблонный тег под конкретную задачу - вывести число опубликованных постов
    """
    return Post.published.count()