from django.shortcuts import render

# Create your views here.
from article.models import Article, Category
from django.http import HttpResponse

from frontuser.models import FrontUser


def index(request):
    # article = Article(title='abc', content='111')
    #
    # category = Category(name="最新文章")
    # category.save()
    # article.category = category
    # article.save()
    article = Article.objects.first()
    print(article.category.name)
    return HttpResponse("success")


def delete_view(request):
    category = Category.objects.get(pk=6)
    category.delete()
    return HttpResponse("delete success")


def one_to_many_view(reuest):
    # 1.一对多的关联操作
    # article = Article(title='测试标题', content='abc')
    # category = Category.objects.first()
    # author = FrontUser.objects.first()
    #
    # article.category = category
    # article.author = author
    # article.save()

    # 2.获取某个分类下所有文章
    # category = Category.objects.first()
    # # articles = category.article_set.all()
    # articles = category.articles.all()
    # for art in articles:
    #     print(art)

    category = Category.objects.first()
    article = Article(title="ccc", content="ddd")
    article.author = FrontUser.objects.first()
    # article.save()

    category.articles.add(article, bulk=False)
    # category.save()
    return HttpResponse("successfully")
