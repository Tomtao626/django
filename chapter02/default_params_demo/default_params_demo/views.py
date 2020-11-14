#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/5/26 23:54
# @Author : Tom_tao
# @Site : 
# @File : views.py
# @Software: PyCharm

from django.http import HttpResponse

book_list = [
    '三国演义',
    '水浒传',
    '西游记',
    '红楼梦'
]

# def index(request):
#     return HttpResponse(book_list[0])
# 指定默认参数page
def books(request,page=0):
    return HttpResponse(book_list[page])

