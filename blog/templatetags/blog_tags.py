from django import template
from ..models import Post

# Создание конкретно-прикладных шаблонных тегов для выполнения конкретных задач

register = template.Library()


@register.simple_tag
def total_posts():
    """
    Вывести число опубликованных постов
    """
    return Post.published.count()


@register.inclusion_tag('blog/post/latest_posts.html')
def show_latest_posts(count=5):
    """
    Отображать последние посты на боковой панели блога
    """
    latest_posts = Post.published.order_by('-publish')[:count]
    return {'latest_posts': latest_posts}