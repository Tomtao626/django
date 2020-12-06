from django.shortcuts import render

# Create your views here.
from article.models import Article, Category
from django.http import HttpResponse


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
