from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    # Представление поста
    path('', views.post_list, name='post_list'),
    # Конвертер пути
    # https://docs.djangoproject.com/en/4.1/topics/http/urls/#registering-custom-path-converters
    path('<int:year>/<int:month>/<int:day>/<slug:posr>/',
         views.post_detail,
         name='post_detail'),
]