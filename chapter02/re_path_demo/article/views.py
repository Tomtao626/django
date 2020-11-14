from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def article(request):
    return HttpResponse("文章首页")

def article_list(request,year):
    text = "你输入的年份是：%s" % year
    return HttpResponse(text)


def article_list_month(request,month):
    text = "你输入的月份是：%s" % month
    return HttpResponse(text)