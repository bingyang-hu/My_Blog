from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render

from .models import ArticlePost


def article_list(request):

    articles = ArticlePost.objects.all()

    context={'articles':articles}

    return render(request,'article/list.html',context)
