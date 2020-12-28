from django.shortcuts import render
from django.http import HttpResponse
from .models import Article
from django.views.decorators.http import require_http_methods, require_GET, require_POST


@require_GET
@require_http_methods(['GET'])
def index(request):
    # 首页返回所有的文章
    articles = Article.objects.all()
    return render(request, 'index.html', context={'articles': articles})


@require_http_methods(['POST', 'GET'])
def add_article(request):
    """post请求新增数据"""
    if request.method == 'GET':
        return render(request, 'add_article.html')
    else:
        title = request.POST.get('title', '')
        content = request.POST.get('content', '')
        Article.objects.create(title=title, content=content)
        return HttpResponse("add success")
