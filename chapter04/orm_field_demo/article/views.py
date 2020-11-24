from django.shortcuts import render
from django.http import HttpResponse
from .models import Article, Person
from django.utils.timezone import now, localtime

# Create your views here.

def index (request):
    # article = Article()
    # article.is_removed = True
    # article.title = "xxx"
    # article.create_time = now()
    # article.save()
    article = Article.objects.get(title='xxx')
    article.title = 'aaaa'
    article.save()
    # create_time = article.create_time
    # print("==="*30)
    # print(create_time)
    # print(localtime(create_time))
    # print("==="*30)
    return HttpResponse("success")
    # return render(request, 'index.html', context={'create_time':create_time})


def email_view(request):
    person = Person()
    person.email = "aaaaaa"
    person.save()
    return HttpResponse("success!")