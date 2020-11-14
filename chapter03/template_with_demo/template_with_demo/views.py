#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/6/1 23:26
# @Author : Tom_tao
# @Site : 
# @File : views.py
# @Software: PyCharm

from django.shortcuts import render

def index(request):
    context = {
        "person":[
            '张三',
            '里斯',
            '王五',
        ]
    }
    return render(request,"index.html",context=context)