from django.http import HttpResponse
from django.shortcuts import render
from article.models import Article, Tag
from .models import User


# Create your views here.

def index(request):
    # article = Article(title='abc', content='1111')
    # author = User.objects.create(username='abcde', password='test112')
    # article.author = author
    # article.save()
    article = Article.objects.first()
    tag1 = Tag.objects.create(name='python')
    tag2 = Tag.objects.create(name='django')
    article.tags.add(tag1, tag2)
    article.save()
    return HttpResponse("success")
