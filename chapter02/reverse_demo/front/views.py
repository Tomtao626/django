from django.shortcuts import render

# Create your views here.

from django.shortcuts import redirect,reverse
from django.http import HttpResponse

def index(request):
    username = request.GET.get('username')
    if username:
        return HttpResponse("前台首页")
    else:
        # login_url = reverse('login')
        # return redirect(login_url)
        # detail_url = reverse('detail',kwargs={'article_id':1})
        # return redirect(detail_url)
        login_url = reverse('login')+"?next=/"
        return redirect(login_url)

def login(request):
    return HttpResponse("登录页面")

def article_detail(request,article_id):
    text = "你的文章id是：%s" % article_id
    return HttpResponse(text)