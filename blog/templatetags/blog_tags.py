from django import template
from ..models import Post
from django.db.models import Count
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


@register.simple_tag
def get_most_commented_posts(count=5):
    """
    Отображать посты с найбольшим количеством комментариев
    """
    return Post.published.annotate(total_comments=Count('comments')
                                   ).order_by('-total_comments')[:count]