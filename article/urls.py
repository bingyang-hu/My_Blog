from django.urls import path
from django.urls import include
from . import views
app_name = 'article'

urlpatterns = [
    path('article-list/',views.article_list,name='article_list'),
]
