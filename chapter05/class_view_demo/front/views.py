from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

from .models import Article


def add_article(request):
    articles = list()
    for x in range(0, 102):
        article = Article(title=f'标题:{x}', content=f'内容:{x}')
        articles.append(article)
    Article.objects.bulk_create(articles)
    return HttpResponse("add success")


class ArticleListView(ListView):
    model = Article
    template_name = 'article_list.html'
    context_object_name = 'articles'
    paginate_by = 10
    ordering = 'add_time'
    page_kwarg = 'p'

    def get_context_data(self, **kwargs):
        # 先调用继承父类ArticleListView的get_context_data()方法
        context = super(ArticleListView, self).get_context_data(*kwargs)
        context['username'] = 'tomtao'
        print(11111111111111111111)
        print(context)
        print(22222222222222222222)
        return context

    # 如果需要对返回的数据进行的过滤 则需要使用get_queryset()方法 不然则默认返回全部数据
    # 即 return Article.objects.all()
    def get_queryset(self):
        # 查询id小于9的数据并返回
        return Article.objects.filter(id__lte=9)
