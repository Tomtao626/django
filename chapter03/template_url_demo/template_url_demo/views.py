#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/6/2 23:02
# @Author : Tom_tao
# @Site : 
# @File : views.py
# @Software: PyCharm

from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, "index.html")


def login(request):
    next = request.GET.get("next")
    text = "登录页面，登陆成功要跳转的url是：%s" % next
    return HttpResponse(text)


def book(request):
    return HttpResponse("图书首页")


def book_detail(request, book_id, category):
    text = "你的图书id是:%s,分类id是:%s" % (book_id, category)
    return HttpResponse(text)


def movie(request):
    return HttpResponse("电影首页")


def city(request):
    return HttpResponse("同城首页")
