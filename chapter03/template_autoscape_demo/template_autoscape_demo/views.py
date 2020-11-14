#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/6/2 23:02
# @Author : Tom_tao
# @Site : 
# @File : views.py
# @Software: PyCharm

from django.shortcuts import render


def index(request):
    context = {
        'info': "<a href='http://www.baidu.com'>百度</a>"
    }
    return render(request, "index.html", context=context)
