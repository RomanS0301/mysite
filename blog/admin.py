from django.contrib import admin
from .models import Post, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'author', 'publish', 'status']  # отображение на странице списка полей
    list_filter = ['status', 'created', 'publish', 'author']  # позволяет фильтровать результаты по полям
    search_fields = ['title', 'body']  # строка поиска
    prepopulated_fields = {'slug': ('title',)}  # предзаполнение поля slug, даннымии вводимыми в title
    raw_id_fields = ['author']  # Поисковый виджет
    date_hierarchy = 'publish'  # навигационные ссылки для навигации по иерархии дат
    ordering = ['status', 'publish']  # атрибуты сортировки по умолчанию


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'post', 'created', 'active']
    list_filter = ['active', 'created', 'updated']
    search_fields = ['name', 'email', 'body']