#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/6/1 22:33
# @Author : Tom_tao
# @Site : 
# @File : views.py
# @Software: PyCharm

from django.shortcuts import render

def index(request):
    # context = {
    #     'age':18,
    # }
    context ={
        "heros":[
            '鲁班',
            '张飞',
            '诸葛亮',
        ]
    }
    return render(request,"index.html",context=context)